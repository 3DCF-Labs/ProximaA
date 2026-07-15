# ProximaA 1.0 — Model Card

## What it is

ProximaA 1.0 is a 32-billion-parameter open-weight language model built to be a strong all-round security assistant. Trained specifically on cybersecurity data, it is purpose-built for the day-to-day work of a security team: detecting vulnerabilities, validating false positives, verifying patches, writing secure fixes, and reasoning about security.

- **Size:** 32.5B parameters
- **Context:** 4096 tokens
- **License:** Apache-2.0 (see `NOTICE.md`)
- **Release date:** 2026-07-15
- **Built by:** Yevhenii Molchanov, 3DCF Labs
- **Organization:** https://github.com/3DCF-Labs

## What it does

- **Detect vulnerabilities.** Given code, it flags security issues and names the likely class.
- **Validate false positives.** It tells a confirmed issue from scanner noise, and says what evidence is needed to be sure.
- **Verify patches.** It checks that a fix addresses the real cause and suggests regression tests.
- **Write secure fixes.** Given a report or code, it finds the root cause and produces a safe, minimal fix with tests.
- **Reason and plan.** It works through audits, detection rules, and remediation steps.

It is trained across web and API security, smart contracts (EVM and non-EVM), supply chain and CI/CD, cloud and infrastructure, and LLM/AI application security.

## What it is not for

ProximaA is a defensive tool. It will not write exploits, attack third-party systems, steal credentials, or help with any offensive operation. See `ACCEPTABLE_USE.md`.

## How good it is

ProximaA 1.0 is strong across the full security workflow — detection, triage, false-positive validation, patch verification, and fixes. Trained specifically on cybersecurity data, it outperforms the open base models it builds on on defensive-security work while keeping strong general reasoning and coding. Measured on standard public benchmarks and an internal security test set.

| Area | Benchmark | Score |
|---|---|---|
| Vulnerability detection (in-domain) | identify + classify held-out issues | 0.97 |
| Secure fixes | internal security fix benchmark | leads its base models |
| Coding | HumanEval (pass@1) | 0.63 |
| Math reasoning | GSM8K | 0.89 |
| Knowledge | MMLU | 0.78 |
| Reasoning | ARC-Challenge | 0.67 |
| Safety — over-refusal | CyberSecEval FRR (lower is better) | 0.025 |
| Safety — attack help | CyberSecEval MITRE (lower is safer) | 0.00 |

Notes:
- **Detection:** on held-out security material in its trained domains, it correctly identifies and classifies vulnerabilities 97% of the time. Generic C/C++ function-classification benchmarks are a known-hard task where no current model does much better than chance; those are not the model's target.
- **Fixes:** on defensive-security fixes it scores higher than the open base models it is built on.
- **Safety:** it refuses all requests for operational attack help (MITRE 0.00) and rarely refuses legitimate security work (2.5% over-refusal).
- **Reasoning:** general reasoning is on par with comparable 32B models — the security focus does not weaken it.

ProximaA is a security specialist. It is not meant to compete with much larger general-purpose models on general tasks; it is meant to be the stronger choice for security work at its size.

## Limitations

- Always have a person review a fix before applying it. The model is an assistant, not a replacement for security review.
- Resistance to prompt-injection attacks is moderate. Do not feed it untrusted input in a setting where that matters without your own guardrails.
- Use it only for authorized, defensive work.

## License and attribution

ProximaA 1.0 is released under Apache-2.0. It is built using open-source components released under Apache-2.0 and MIT. Full attribution is in `NOTICE.md`.

## Citation

```
ProximaA 1.0
Yevhenii Molchanov, 3DCF Labs
https://github.com/3DCF-Labs
2026
```
