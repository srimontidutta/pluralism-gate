# Machine-readable tables

This directory contains CSV and JSON versions of the compact tables used by the repository.

- `gate-regimes.csv` records the four Gate regimes and their conditions.
- `protocol-properties.csv` records the four implementation properties.
- `stress-tests.csv` and `stress-tests.json` contain the six Table 2 cases.
- `counterfactual-tests.csv` and `counterfactual-tests.json` contain the six Table 4 perturbations.
- `audit-fields.csv` lists the eight fields in the minimal decision record.

The CSV files are convenient for analysis and annotation pipelines; the JSON files preserve the same test content for tools that prefer structured objects. The `PG-ST` and `PG-CF` identifiers are repository labels used consistently across the corresponding Markdown and data files.
