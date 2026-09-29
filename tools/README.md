# Validation tool

`validate_record.py` performs semantic checks across fields in a complete decision record and uses only the Python standard library.

Validate the worked records with:

```bash
python tools/validate_record.py examples/valid/*.json
```

The validator checks proposition and stakeholder references, two-sided support for every proposition in `conflict_set`, warrant coverage, consultation-route completeness, Gate invocation status, and the regime implied by the decision rule.

The records in `examples/negative-tests/` are expected to fail:

```bash
python tools/validate_record.py examples/negative-tests/*.json
```
