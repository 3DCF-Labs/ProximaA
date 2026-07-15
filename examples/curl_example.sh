#!/usr/bin/env bash
# ProximaA 1.0 — curl example against an OpenAI-compatible server
# (llama.cpp `llama-server`, vLLM, or Ollama on :11434).
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8080/v1}"
MODEL="${MODEL:-proximaa-1.0}"

SYSTEM="You are a defensive secure-code assistant. Analyze only authorized code and produce safe fixes. Do not provide exploit code or attack assistance."

read -r -d '' USER <<'EOF' || true
Review this vulnerability report and provide a defensive fix.

Title: API key lookup returns objects by ID without tenant ownership validation
Language: Go / HTTP API / SQL
Vulnerability class: broken object-level authorization (IDOR)
Context: The handler loads an API key by ID only; the tenant in the request
path is ignored, and the query filters only by id and deletion state.
EOF

curl -s "${BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg m "$MODEL" --arg s "$SYSTEM" --arg u "$USER" '{
        model: $m,
        temperature: 0,
        max_tokens: 1536,
        messages: [ {role:"system", content:$s}, {role:"user", content:$u} ]
      }')" \
  | jq -r '.choices[0].message.content'
