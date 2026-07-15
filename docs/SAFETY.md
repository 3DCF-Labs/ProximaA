# Safety

ProximaA 1.0 is built to be safe by default.

- **Defensive by design.** It focuses on root cause, safe fixes, and tests. It refuses requests for operational attack help.
- **Tested.** On the CyberSecEval 4 safety benchmark it gave no operational attack help (score 0.00) and rarely over-refused legitimate security work (2.5%).
- **Clean training.** The training data contains no exploit payloads and is limited to defensive material.

## What to keep in mind

- Have a person review any fix before you apply it.
- Resistance to prompt-injection is moderate; add your own input controls if you process untrusted content.
- The model is not a security guarantee. Use it as one part of a review process.
