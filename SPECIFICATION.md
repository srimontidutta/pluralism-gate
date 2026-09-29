# Pluralism Gate Specification

This document presents the paper's formal framework in an implementation-facing form while preserving its original scope.

## 1. Decision instance

A decision instance is

`d = (x, c, A_d, H_d, Q_d)`

where `x` is the task, `c` is the decision context, `A_d` is the feasible action set, `H_d` is the set of potentially relevant stakeholders, and `Q_d` contains the action-relevant propositions on which reasons may bear.

## 2. Scope of Gate-triggering conflict

Let `Q_d^V ⊆ Q_d` contain propositions for which surviving two-sided support, after domain-appropriate evidential screening, represents residual normative or action-justificatory disagreement. Purely empirical disagreement remains with the domain's evidential or uncertainty procedure. For mixed empirical-normative claims, the Gate concerns the residual normative or action-justificatory component that remains after evidential screening.

## 3. Standing relation

A deployment policy `Π` supplies a standing relation

`S_{Π,d} ⊆ H_d × Q_d^V`.

A pair `(h, q) ∈ S_{Π,d}` means that stakeholder `h` has a recognized basis for bearing on proposition `q` in decision `d`. The paper allows this basis to arise from affectedness, jurisdiction or delegated authority, epistemic position, rights or entitlement, or another domain-specific rule. The policy records the basis without reducing these forms of standing to a single scalar weight.

## 4. Reason attribution and admissibility

Let `src_d(r) ⊆ H_d` identify the stakeholder or stakeholders to whom reason `r` is attributable. A reason concerning proposition `q` is standing-qualified when at least one attributable stakeholder has standing for that proposition under `S_{Π,d}`.

For each proposition `q`, `R^+_Π(q,d)` contains material admissible reasons supporting `q`, while `R^-_Π(q,d)` contains material admissible reasons supporting `¬q`.

The evidential filter removes reasons whose factual premises fail the applicable evidence standard. The standing filter applies the declared relation between stakeholders and propositions. The materiality rule excludes reasons too weak or remote to affect the contemplated choice under the same policy. Together, these filters separate factual defeat, stakeholder relevance, and residual normative conflict before the authority question is evaluated.

## 5. Standing-qualified information state

Define

` s_Π(q,d) = 1[R^+_Π(q,d) ≠ ∅] `

and

` o_Π(q,d) = 1[R^-_Π(q,d) ≠ ∅] `.

The information state `v_Π(q,d) = (s_Π(q,d), o_Π(q,d))` takes one of four values:

| State | Value | Interpretation |
| --- | ---: | --- |
| `S` | `(1,0)` | support only |
| `O` | `(0,1)` | opposition only |
| `B` | `(1,1)` | material reasons remain on both sides |
| `N` | `(0,0)` | neither side retains a material admissible reason |

The paper uses the four-valued structure as an information representation. A `B` state records surviving material standing-grounded conflict without assigning equal probability, prevalence, or normative weight to either side.

## 6. Unresolved conflict set

The unresolved conflict set is

`B_Π(d) = {q ∈ Q_d : v_Π(q,d) = B}`.

A nonempty `B_Π(d)` means that at least one material action-relevant proposition retains admissible standing-grounded reasons on both sides. States `S` and `O` contain no surviving two-sided conflict, while state `N` is handled through the domain's rules for missing information or abstention.

## 7. Resolution warrant

Let `W_Π(d) ∈ {0,1}` be true exactly when the deployment policy recognizes a sufficient resolution warrant for the contested commitment under review. A sufficient warrant covers every material unresolved conflict in `B_Π(d)` that bears on that commitment, so sufficiency is evaluated at the decision level.

The paper gives examples that include an explicit user choice in a user-controlled domain, a binding jurisdictional rule treated as controlling among otherwise feasible alternatives, a rights-protecting priority rule recognized by the deployment policy, contractually delegated authority, and a tie-breaking procedure accepted before the conflict arose.

Rules that determine feasibility or independent permissibility remain part of the feasible action set or surrounding task policy. A rule functions as a resolution warrant when the declared policy treats it as authority for choosing among still-feasible contested alternatives. Repetition and numerical prevalence in retrieved material do not constitute warrants.

When a task contains independently contested commitments governed by different warrants, each commitment is evaluated as a separate decision instance.

## 8. Premature value collapse

Let `Commit_A(d)` indicate that agent `A` selects, recommends as controlling, or executes a single contested option. Premature value collapse is

`PVC_{Π,A}(d) ⇔ B_Π(d) ≠ ∅ ∧ Commit_A(d) ∧ ¬W_Π(d)`.

The definition permits commitment in the presence of unresolved disagreement when the declared policy supplies sufficient authority for the commitment.

## 9. The Pluralism Gate

The Gate applies when `B_Π(d) ≠ ∅`.

Let `Req(d)` indicate that the current task requires commitment to a contested option, and let `C_Π(d)` indicate that a policy-recognized consultation path is available before commitment and could materially supply or clarify the authority needed to resolve the conflict.

| Regime | Condition | Operational interpretation |
| --- | --- | --- |
| `REPRESENT` | `¬Req(d)` | The task calls for presentation rather than commitment, so the material conflict is preserved for the user or downstream decision-maker. |
| `RESOLVE` | `Req(d) ∧ W_Π(d)` | Commitment is required and a sufficient warrant covers every material unresolved conflict relevant to the commitment. |
| `CONSULT` | `Req(d) ∧ ¬W_Π(d) ∧ C_Π(d)` | Commitment is required, a sufficient warrant is absent, and a recognized stakeholder or decision-maker can materially supply or clarify the needed authority before action. |
| `DEFER` | otherwise | Commitment is required, a sufficient warrant is absent, and no policy-valid consultation path can close the authority gap in time. |

## 10. Scope of the decision rule

The Gate determines whether unresolved pluralism permits unilateral commitment, while the surrounding system continues to enforce other requirements. A jurisdictional rule may authorize `RESOLVE` while a separate safety rule prohibits the contemplated action. Consultation may establish a user's preference in travel planning while cost or accessibility requirements continue to constrain the resulting booking.

The framework thereby keeps authority over a contested commitment explicit without turning the Gate into a complete policy for the underlying task.
