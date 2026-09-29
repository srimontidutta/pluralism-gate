# Worked examples

This directory contains machine-readable examples built around the specification cases in Table 2.

- `valid/` contains complete decision records that can be checked with the semantic validator. A small number of records include an explicit `notes` field where a machine-readable example needs a detail that the short table entry leaves implicit.
- `incomplete-examples/` contains compact records for cases that stop before every decision-record field can be populated from the case description.
- `negative-tests/` contains structurally complete records with intentionally incorrect Gate outcomes. They are useful for testing whether an implementation detects semantic failures rather than merely parsing the JSON.

The stress-test descriptions themselves remain in [`../stress-tests/`](../stress-tests/); these files show how those cases can be represented as data.
