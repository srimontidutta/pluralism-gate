# Specification stress tests

Table 2 uses six cases to exercise different parts of the framework: evidential screening, standing, consultation, resolution warrants, and tasks that require presentation rather than commitment. The `PG-ST` identifiers provide short references for the repository and evaluation reports.

| ID | Case | Expected disposition |
| --- | --- | --- |
| `PG-ST1` | Medical factual dispute | Ordinary resolution; Gate not invoked |
| `PG-ST2` | Local service relocation | `CONSULT` |
| `PG-ST3` | Indigenous land-use decision | `DEFER` |
| `PG-ST4` | Personal travel planning | `CONSULT` |
| `PG-ST5` | Content rule under explicit jurisdiction | `RESOLVE` |
| `PG-ST6` | Advisory urban-design brief | `REPRESENT` |

The medical case is resolved through evidential screening before the Gate is reached. The remaining cases cover each of the four Gate regimes without introducing case-specific branches into the decision rule.

Each case has a short standalone description in this directory, and CSV/JSON copies of the table are available in [`../data/`](../data/).
