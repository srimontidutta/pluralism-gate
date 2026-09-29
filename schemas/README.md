# Decision-record schema

`decision-record.schema.json` provides a JSON representation of the eight audit fields in Table 3. Stable proposition, stakeholder, and reason identifiers make it possible to compare records across implementations while keeping the underlying standing and warrant policies explicit.

The schema links standing records and reasons to propositions, records reason polarity and attribution, carries proposition identifiers into `conflict_set`, represents `Req(d)` as a boolean task state, and gives consultation and resolution warrants structured records. `gate_outcome.regime` is restricted to the four Gate regimes whenever the Gate is invoked.

An optional top-level `notes` array can be used for modeling choices or implementation context that are useful when reading a worked record. Additional implementation-specific fields remain permitted so that the compact decision record can sit inside a richer system trace.

Cross-field semantics are checked by [`../tools/validate_record.py`](../tools/validate_record.py), which verifies reference integrity, two-sided conflict representation, warrant coverage, consultation-route completeness, and consistency between the recorded Gate inputs and outcome.
