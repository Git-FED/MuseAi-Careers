# Relay setup

The relay is a message boundary, not a permission bypass. Keep it private, authenticated, rate-limited, and observable.

## Message contract

```json
{"agent":"agent-id","type":"heartbeat|task|result|alert","timestamp":"ISO-8601","status":"active|paused|error","payload":{}}
```

## Minimum controls

1. Use short-lived credentials and least privilege.
2. Reject messages with unknown agent IDs or stale timestamps.
3. Log task IDs, not private content by default.
4. Require human approval for money movement, account changes, wagers, and sensitive publication.
5. Provide a kill switch and replay-safe task IDs.
6. Do not put API keys, wallet seeds, cookies, or personal data in relay payloads.
