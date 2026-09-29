# Negative tests

These records are structurally complete but intentionally report Gate outcomes that conflict with the decision rule.

`resolve-without-warrant.json` reports `RESOLVE` even though material conflict remains and the record contains no sufficient warrant. `represent-despite-required-commitment.json` reports `REPRESENT` even though commitment is required and a policy-valid consultation path is available.

They are intended to fail semantic validation and can be used when testing evaluators or controller checks.
