#!/usr/bin/env python3
"""
ProximaA 1.0 — minimal mode client.

Loads the six built-in security modes from ../prompts/modes.json and sends a
request to any OpenAI-compatible endpoint (llama.cpp server, vLLM, Ollama).

Examples:
    # llama.cpp server on :8080
    python proximaa_client.py --mode fix --input report.txt

    # vLLM
    python proximaa_client.py --base-url http://localhost:8000/v1 \
        --model proximaa-1.0 --mode detect --input snippet.c

    # Ollama
    python proximaa_client.py --base-url http://localhost:11434/v1 \
        --model proximaa --mode triage --input finding.md
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

MODES_PATH = Path(__file__).resolve().parent.parent / "prompts" / "modes.json"


def load_modes():
    with open(MODES_PATH) as f:
        return json.load(f)["modes"]


def build_messages(modes, mode, user_input):
    if mode not in modes:
        sys.exit(f"unknown mode '{mode}'. available: {', '.join(modes)}")
    m = modes[mode]
    # each mode's user_template has one {placeholder}; fill it with the input
    user = re.sub(r"\{[a-z_]+\}", lambda _: user_input, m["user_template"], count=1)
    return [
        {"role": "system", "content": m["system"]},
        {"role": "user", "content": user},
    ]


def chat(base_url, model, messages, max_tokens, temperature):
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }).encode()
    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        data = json.load(r)
    return data["choices"][0]["message"]["content"]


def main():
    p = argparse.ArgumentParser(description="ProximaA 1.0 mode client")
    p.add_argument("--mode", required=True,
                   help="detect | triage | validate | fix | verify | plan")
    p.add_argument("--input", help="path to input file (default: stdin)")
    p.add_argument("--base-url", default="http://localhost:8080/v1")
    p.add_argument("--model", default="proximaa-1.0")
    p.add_argument("--max-tokens", type=int, default=1536)
    p.add_argument("--temperature", type=float, default=0.0)
    args = p.parse_args()

    user_input = Path(args.input).read_text() if args.input else sys.stdin.read()
    modes = load_modes()
    messages = build_messages(modes, args.mode, user_input)
    print(chat(args.base_url, args.model, messages, args.max_tokens, args.temperature))


if __name__ == "__main__":
    main()
