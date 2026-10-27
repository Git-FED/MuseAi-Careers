# Identity and account boundaries

Each agent should have a documented owner, purpose, platform, permission set, recovery method, and deprovisioning path.

Use dedicated accounts only where allowed by the platform. Do not fabricate identities, evade verification, or operate duplicate accounts to defeat enforcement. Keep recovery contacts and secrets outside Git. Rotate credentials after staff or agent changes.

| Identity | Purpose | Owner | Access | Status |
|---|---|---|---|---|
| Primary social account | Public publishing | TBD | Scoped session | Replace |
| Relay service account | Heartbeats/tasks | TBD | Least privilege | Replace |
| Payment account | Settlement only | TBD | Human-controlled | Replace |
