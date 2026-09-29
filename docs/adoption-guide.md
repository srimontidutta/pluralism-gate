# Adoption guide

The Pluralism Gate can be placed at several points in an agent system. The useful location is one where material conflict is still represented explicitly and the system has not yet made the contested commitment.

## Pre-action policy check

A controller can apply the Gate immediately before an action, recommendation, or other contested commitment. The check uses the current conflict set, task requirement, warrant status, and consultation availability to determine the permitted regime.

This placement is particularly simple when an existing controller already has a final policy or safety check. The Gate can be evaluated alongside those checks while retaining its narrower role: it answers the authority question created by unresolved standing-grounded conflict.

## Deliberation step

The Gate can also operate as an intermediate stage after evidential screening and standing qualification. This keeps material disagreement available through retrieval and synthesis rather than allowing a majority signal or a single generated answer to settle the choice implicitly.

An implementation at this stage should preserve enough information to reconstruct which propositions remain in `B_Π(d)`, which stakeholders supply standing-qualified reasons, and which warrant or consultation rule is being applied.

## Evaluator

The decision rule and protocol properties can be applied to completed traces. An evaluator can examine whether a change in regime follows a corresponding change in standing, evidence, warrant status, consultation availability, or task requirements.

This is useful even when the system being evaluated does not implement the Gate internally. A trace can be converted into the audit-record format and checked against the declared policy after the fact.

## Auditable agent trace

The eight fields in Table 3 provide a compact record of the propositions, standing, admissible reasons, conflict set, task state, consultation route, resolution warrant, and Gate outcome. The record can accompany a richer trace containing tool calls, intermediate reasoning artifacts, or application-specific metadata.

## Benchmark use

The paper proposes four annotation layers for benchmark scenarios: evidential status, candidate stakeholder claims, an explicit standing profile, and any applicable resolution warrant. When standing is contested, several declared policy profiles can be retained for the same scenario. This allows the same underlying case to be evaluated under different policies without turning a policy disagreement into a single gold label.

## Retrieval asymmetry studies

Matched multilingual or geographically imbalanced retrieval variants can be used to examine whether a standing-grounded perspective disappears because it is less retrievable or because the declared policy excludes it. Sparse representation may reflect publication access, language coverage, or institutional visibility, so retrieval coverage should be analyzed separately from stakeholder standing.
