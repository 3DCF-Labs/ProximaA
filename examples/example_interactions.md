# Example interactions

These show the kind of input ProximaA 1.0 takes and the answers it gives.

## Example 1

**Ask:** Review this finding and give a defensive fix — Account confusion / missing signer or ownership check

**ProximaA 1.0:**

```
### Finding
Solana instruction fails to validate signer, owner, PDA, or sysvar account identity
### Vulnerability class
Account confusion / missing signer or ownership check
### Root cause
A Solana program accepts accounts that satisfy a shape but not the intended identity, signer, owner, or PDA derivation constraints. Attackers can substitute lookalike accounts or spoof sysvars if checks are incomplete.
### Safe code fix
Validate every account by identity, owner, signer, PDA seeds, bump, and sysvar address. Use Anchor constraints where appropriate and fail closed on any mismatch. Add tests for missing signer, wrong owner, spoofed PDA, and spoofed sysvar.
### Regression tests
Add program tests for: expected accounts work; missing signer fails; wrong owner fails; wrong PDA fails; spoofed sysvar fails; malicious lookalike account fails.

### Patch sketch
```rust
assert!(signer.key == expected_signer);
assert!(account.owner == expected_owner);
assert!(Pubkey::create_with_seed(...).unwrap() == pda.key);
assert!(sysvar.address == anchor_sysvar::clock::ID);
```### False-positive / neutralization checks
False positive if the program intentionally accepts any account of a certain type without identity validation and documents that decision with tests.
### Safety boundary
Keep analysis defensive: validate reachability, patch the sink or authorization boundary, and avoid instructions that would enable unauthorized exploitation. Regression tests should assert the neutralizing control is on the data path. Do not add exploit-oriented behavior to the target system.
```

## Example 2

**Ask:** Review this finding and give a defensive fix — Remote code execution through argument injection

**ProximaA 1.0:**

```
### Finding
CVE-2024-4577: PHP-CGI on Windows treats crafted request data as process arguments
### Vulnerability class
Remote code execution through argument injection
### Root cause
A CGI deployment path on Windows lets request data influence interpreter argument parsing because platform character conversion and process invocation semantics are not safely constrained.
### Safe code fix
Do not use CGI on Windows for untrusted requests. Run PHP as a module or FastCGI with a fixed interpreter path. Apply the vendor patch and restrict exposure until migration is complete.
### Example defensive patch direction
```text
Use php-fpm or CGI disabled on Windows; patch PHP 8.3/8.4/8.5; WAF double quotes and backslashes as compensating controls.
```
### Regression tests
- CGI handler is disabled or not reachable from untrusted users.
- Request bodies containing metacharacters are rejected or passed as opaque data.
- Static and dynamic inventory checks confirm no Windows CGI exposure remains.
### Security boundary
Keep validation defensive. Do not add exploit payloads, offensive automation, credential theft, persistence, stealth, or third-party attack instructions to the training target. Use this only for authorized defensive review, patching, regression testing, and triage.
```

