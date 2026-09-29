#!/usr/bin/env python3
"""Semantic validator for Pluralism Gate decision records.

Usage:
    python tools/validate_record.py path/to/record.json
    python tools/validate_record.py examples/valid/*.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REGIMES = {"REPRESENT", "RESOLVE", "CONSULT", "DEFER"}


def expected_regime(record: dict):
    conflict = bool(record.get("conflict_set"))
    if not conflict:
        return None
    req = bool(record["task_state"]["requires_commitment"])
    warrant = bool(record["resolution_warrant"]["sufficient"])
    consult = bool(record["consultation"]["available"])
    if not req:
        return "REPRESENT"
    if warrant:
        return "RESOLVE"
    if consult:
        return "CONSULT"
    return "DEFER"


def validate(record: dict) -> list[str]:
    errors: list[str] = []

    prop_ids = [p.get("proposition_id") for p in record.get("decision_propositions", [])]
    prop_set = {p for p in prop_ids if p}
    if len(prop_ids) != len(set(prop_ids)):
        errors.append("decision_propositions contains duplicate proposition_id values")

    standing_pairs = set()
    stakeholder_ids = set()
    for item in record.get("standing", []):
        sid = item.get("stakeholder_id")
        pid = item.get("proposition_id")
        if pid not in prop_set:
            errors.append(f"standing references unknown proposition_id: {pid}")
        stakeholder_ids.add(sid)
        standing_pairs.add((sid, pid))

    reason_ids = []
    polarities_by_prop = {}
    for reason in record.get("admissible_reasons", []):
        rid = reason.get("reason_id")
        pid = reason.get("proposition_id")
        reason_ids.append(rid)
        if pid not in prop_set:
            errors.append(f"reason {rid} references unknown proposition_id: {pid}")
        polarity = reason.get("polarity")
        polarities_by_prop.setdefault(pid, set()).add(polarity)
        for sid in reason.get("attributed_stakeholders", []):
            if (sid, pid) not in standing_pairs:
                errors.append(
                    f"reason {rid} attributes stakeholder {sid} without a standing record for proposition {pid}"
                )
    if len(reason_ids) != len(set(reason_ids)):
        errors.append("admissible_reasons contains duplicate reason_id values")

    conflict = record.get("conflict_set", [])
    for pid in conflict:
        if pid not in prop_set:
            errors.append(f"conflict_set references unknown proposition_id: {pid}")
        pol = polarities_by_prop.get(pid, set())
        if not {"support", "oppose"}.issubset(pol):
            errors.append(
                f"conflict proposition {pid} lacks both support and oppose reasons"
            )

    warrant = record.get("resolution_warrant", {})
    if warrant.get("sufficient"):
        basis = warrant.get("authority_basis")
        if not basis:
            errors.append("sufficient resolution warrant requires authority_basis")
        covered = set(warrant.get("covers_conflicts", []))
        missing = set(conflict) - covered
        if missing:
            errors.append(
                "sufficient resolution warrant does not cover conflict_set: "
                + ", ".join(sorted(missing))
            )

    consult = record.get("consultation", {})
    if consult.get("available") and not consult.get("route"):
        errors.append("available consultation requires a route")

    outcome = record.get("gate_outcome", {})
    invoked = bool(outcome.get("gate_invoked"))
    regime = outcome.get("regime")

    if bool(conflict) != invoked:
        errors.append(
            "gate_outcome.gate_invoked must be true exactly when conflict_set is nonempty"
        )

    expected = expected_regime(record)
    if expected is None:
        if regime is not None:
            errors.append("regime must be null when the Gate is not invoked")
    else:
        if regime not in REGIMES:
            errors.append(f"unknown Gate regime: {regime}")
        if regime != expected:
            errors.append(f"reported regime {regime} conflicts with Eq. 9; expected {expected}")

    return errors


def main(paths: list[str]) -> int:
    if not paths:
        print("usage: validate_record.py RECORD.json [RECORD.json ...]", file=sys.stderr)
        return 2
    failed = 0
    for raw in paths:
        path = Path(raw)
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
            errors = validate(record)
        except Exception as exc:
            errors = [f"could not parse record: {exc}"]
        if errors:
            failed += 1
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
