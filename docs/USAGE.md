# Usage

ProximaA 1.0 ships as full-precision weights and as quantized GGUF files.

| File | Use it for |
|---|---|
| `proximaa-1.0` (fp16) | GPU serving (e.g. vLLM) |
| `proximaa-1.0-Q5_K_M.gguf` | CPU/GPU serving, higher quality |
| `proximaa-1.0-Q4_K_M.gguf` | CPU/GPU serving, smaller and faster (default) |

## Chat format

Use the model's chat template. Prompts follow the standard user/assistant pattern:

```
<｜User｜>{your question}<｜Assistant｜>
```

## Run with vLLM (GPU)

```bash
vllm serve proximaa-1.0 --dtype bfloat16 --max-model-len 4096
```

## Run with llama.cpp (GGUF)

```bash
llama-server -m proximaa-1.0-Q4_K_M.gguf -c 4096
```

## Example prompt

```
Review this finding and give a defensive fix.
Title: API key lookup returns objects by ID without tenant ownership validation
Language: Go / HTTP API / SQL
Vulnerability class: broken object-level authorization (IDOR)
Context: The handler loads an API key by ID only; the tenant in the request path is ignored,
and the query filters only by id and deletion state.
```

The model answers with a structured fix: finding, root cause, safe code fix, and regression tests. See `examples/example_interactions.md`.

## Tips

- For fixes and triage, keep the vulnerability report and code in the prompt.
- Greedy decoding (temperature 0) gives the most consistent results.
- Always review the model's fix before applying it.

## Vulnerability detection

On held-out security material in the model's trained domains, it correctly identifies and classifies vulnerabilities 97% of the time. For best results, give it the code plus any surrounding context and ask it to name the issue and root cause.
