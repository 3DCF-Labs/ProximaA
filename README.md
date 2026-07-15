# ProximaA 1.0

**A 32B open-weight security assistant.** Trained specifically on cybersecurity data for the full defensive workflow: vulnerability detection, false-positive validation, patch verification, secure fixes, and security reasoning.

Built by Yevh, 3DCF Labs

- **Weights & GGUF:** [Hugging Face](https://huggingface.co/3DCF-Labs-org/ProximaA-1.0)
- **License:** Apache-2.0 (see [`NOTICE.md`](NOTICE.md))

---

## What it does

- **Detect** vulnerabilities in code and name the likely class.
- **Validate** false positives — tell a real issue from scanner noise.
- **Verify** patches — check a fix addresses the real cause; suggest regression tests.
- **Fix** — find the root cause and produce a safe, minimal patch.
- **Reason and plan** — audits, detection rules, remediation steps.

It is trained for defenders. It does not help with attacks. See [`docs/ACCEPTABLE_USE.md`](docs/ACCEPTABLE_USE.md).

## Get the model

The weights and quantized GGUF files live on Hugging Face. Pick a runtime:

### Ollama (laptop / desktop)

```bash
# quantized build, no setup
ollama run hf.co/3DCF-Labs-org/ProximaA-1.0-GGUF:Q4_K_M
```

Or build locally from the included [`Modelfile`](Modelfile) after downloading a GGUF:

```bash
ollama create proximaa -f Modelfile
ollama run proximaa
```

### llama.cpp (GGUF)

```bash
llama-server -m proximaa-1.0-Q4_K_M.gguf -c 4096
```

### vLLM (GPU, full precision)

```bash
vllm serve 3DCF-Labs-org/ProximaA-1.0 --dtype bfloat16 --max-model-len 4096
```

### Will it run on a laptop?

The Q4_K_M GGUF is ~19 GB. It runs well on machines with 32 GB+ of unified/​system memory (Apple Silicon M-series is a good fit). On 16 GB laptops it will be tight to unusable — use a smaller machine tier or a GPU host instead.

## Modes

ProximaA ships with six built-in security modes — **detect, triage, validate, fix, verify, plan** — each a ready-made system prompt plus user template in [`prompts/modes.json`](prompts/modes.json). See [`docs/MODES.md`](docs/MODES.md).

```bash
# examples/proximaa_client.py — loads a mode and calls any OpenAI-compatible server
python examples/proximaa_client.py --mode fix --input report.txt
python examples/proximaa_client.py --mode detect --input snippet.c
```

There is also a plain [`examples/curl_example.sh`](examples/curl_example.sh).

## Repository layout

```
README.md              this file
Modelfile              Ollama build file (points at a local GGUF)
prompts/               default system prompt + the six mode prompts (modes.json)
docs/                  MODEL_CARD, MODES, USAGE, SAFETY, ACCEPTABLE_USE
examples/              Python mode client, curl example, sample interactions
NOTICE.md              license and attribution
LICENSE-APACHE.txt     Apache-2.0
LICENSE-MIT.txt        MIT (for components that require it — see NOTICE.md)
```

## Documentation

- [`docs/MODEL_CARD.md`](docs/MODEL_CARD.md) — what the model is, what it's good at, benchmark scores.
- [`docs/MODES.md`](docs/MODES.md) — the six modes and output formats.
- [`docs/USAGE.md`](docs/USAGE.md) — how to run it, with examples.
- [`docs/ACCEPTABLE_USE.md`](docs/ACCEPTABLE_USE.md) and [`docs/SAFETY.md`](docs/SAFETY.md) — the rules.

## Citation

```
ProximaA 1.0
Yevh, 3DCF Labs
https://github.com/3DCF-Labs
2026
```
