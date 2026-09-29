# Evaluation Guide

The paper presents the Pluralism Gate as a target for model specifications, agent controllers, and evaluations. The sequence below arranges the formal objects and test artifacts into a reproducible evaluation procedure.

## 1. Define the decision instance

Record the task, context, feasible action set, potentially relevant stakeholders, and action-relevant propositions.

## 2. Apply the domain evidential procedure

Identify the propositions for which surviving two-sided support represents residual normative or action-justificatory disagreement. For mixed empirical-normative claims, retain the residual normative or action-justificatory component after evidential screening.

## 3. Apply the declared standing relation

Record the stakeholders considered and the policy basis under which their reasons bear on each proposition. Record the basis for inclusions and exclusions that change the conflict set so later analysis can distinguish changes caused by standing, evidence, or materiality.

## 4. Construct the information state

For each relevant proposition, determine whether material admissible support and opposition remain after the evidential, standing, and materiality filters. The resulting state is `S`, `O`, `B`, or `N`.

## 5. Construct the unresolved conflict set

Collect propositions in state `B` into `B_Π(d)`. An empty set returns the decision to the surrounding domain procedure, while a nonempty set invokes the Gate.

## 6. Record task, warrant, and consultation status

For the contested commitment under review, record whether the task requires commitment, whether a sufficient resolution warrant exists, and whether a policy-valid consultation path can materially supply or clarify the needed authority before action.

## 7. Apply the Gate

Use the decision rule in [`SPECIFICATION.md`](../SPECIFICATION.md) to obtain `REPRESENT`, `RESOLVE`, `CONSULT`, or `DEFER`.

## 8. Record and validate the audit fields

Populate the eight fields in the minimal audit record. The repository schema supplies a common serialization, while [`tools/validate_record.py`](../tools/validate_record.py) checks the principal cross-field relationships and the regime implied by Eq. 9.

## 9. Run specification stress tests

Apply the six Table 2 cases to examine whether the implementation separates evidence, standing, authority, and task structure as specified.

## 10. Run counterfactual tests

Apply the Table 4 perturbations to examine whether the implementation responds appropriately when prevalence, standing, evidence, warrant status, task requirements, or stakes change.

## 11. Report policy context

A benchmark should retain the declared standing profile and applicable warrant policy. When several standing policies are under study, results can be reported separately for each profile. This structure supports technical comparison of protocol compliance while preserving the policy assumptions needed for governance analysis.
