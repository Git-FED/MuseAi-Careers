# Muse AI Careers

<img width="1284" height="699" alt="Screenshot 2026-10-27 113132" src="https://github.com/user-attachments/assets/7cd3a169-c311-404f-a808-6f40bac12063" />

> **Give your AI a job. Publish the work record.**

Muse AI Careers is a practical catalog of autonomous-agent jobs, operating notes, skill files, and verification records. It is not a university, a picks shop, or a promise of passive income. The goal is simple: document systems that have been attempted, separate observed results from projections, and ship portable instructions that another operator can inspect and rerun.

## Current status

| Track | Status | What is actually claimed |
|---|---|---|
| [01 Omnipresence Engine](jobs/01-omnipresence/) | Live / operator-controlled | Social distribution and community-growth workflows; platform rules and consent apply. |
| [02 Multi-Sport Quant Desk](jobs/02-sports-quant/) | Live / human execution | Data collection, formula execution, and recordkeeping. A human places any wager. |
| [03 Video / Image Editor](jobs/03-video-editor/) | In development | High-volume creative production workflows; not certified for live placement. |
| [04 Crypto Swarm](jobs/04-crypto-swarm/) | Fleet provisioned / pending execution | A proposed micro-yield experiment. No measured mining P&L is included here. |
| [05 Open Track](jobs/05-open-track/) | Accepting proposals | A place to propose a new agent job with boundaries and an evaluation plan. |

<img width="1287" height="701" alt="Screenshot 2026-10-27 113229" src="https://github.com/user-attachments/assets/c81f66c1-f388-4c1e-8de2-4c7fdfa7b020" />

## The operating thesis

People do not need another prompt collection. They need a worker with a defined job, an explicit ceiling, observable outputs, and a record that does not hide failures. Every track in this repository therefore includes:

- a job description and human/agent boundary;
- a versioned skill file;
- operating procedures and practice reps;
- an evaluation plan;
- a work-record template for observed evidence;
- a risk and compliance section.

## What this repository does not promise

- No guaranteed income, profit, win rate, conversion rate, or return.
- No “zero-risk” financial outcome. Cloud costs, platform bans, fees, taxes, and market losses are real risks.
- No automatic betting, wallet control, or financial execution.
- No spam, evasion, mass-account abuse, or bypassing platform safeguards.
- No legal, medical, tax, investment, or gambling advice.

The phrase “it will work very poorly” is useful here as an anti-hype standard: a system can be technically plausible while still being uneconomic. Measure both output and total cost before calling a track successful.

<img width="1280" height="696" alt="Screenshot 2026-10-27 113247" src="https://github.com/user-attachments/assets/1581f9d3-bc87-4797-86d9-e08daaff156e" />

## Proof over promises

A work record should distinguish:

1. **Observed:** directly supported by a dated log, screenshot, export, or transaction record.
2. **Reported:** supplied by an operator but not independently checked.
3. **Projected:** a model, estimate, or scenario that has not happened yet.
4. **Pending:** a track that has a plan but no execution evidence.

The repository currently treats the crypto-mining numbers as a projection, not revenue. The 20-account fleet and the 4–8 cents/day estimate are planning context until a compliant deployment produces measured hashrate, payout, uptime, and net-cost records.

## Marketplace

[`hire.html`](hire.html) is a static, Stripe-ready catalog mockup. It contains placeholders only. Replace payment links, service descriptions, refund terms, privacy notices, and availability claims after verifying them. Never publish credentials or private account identifiers in this repository.

<img width="1282" height="698" alt="Screenshot 2026-10-27 113219" src="https://github.com/user-attachments/assets/7f6599f3-ac20-4329-8350-7c068cba0e56" />

## Quick start

```bash
git clone <your-repository-url>
cd muse-ai-careers
python3 -m http.server 8080
# open http://localhost:8080/hire.html
```

Review the track README and `SKILL.md` before operating anything. Copy `.env.example` only into a private runtime environment; it intentionally contains no secrets.

## Repository map

- `jobs/` — the five agent-job tracks.
- `certifications/` — evidence templates and current verification notes.
- `infrastructure/` — relay, VM, and identity operating notes.
- `prompts/` — reusable role prompts, written as bounded operating contracts.
- `marketplace/` — future listing schema and intake notes.
- `docs/` — contribution, safety, and evidence standards.

<img width="1280" height="699" alt="Screenshot 2026-10-27 113213" src="https://github.com/user-attachments/assets/3538fd50-b2e3-4b0f-b1a7-a787494fdada" />

## The “fake school” idea, made concrete

A diploma is a claim made by an institution. A work record is evidence someone can inspect. Muse keeps the useful part of certification—the skill file, test set, version, and record—and drops the implication that a badge can guarantee a result. If this project disappears, a properly packaged skill file and its evidence should remain usable by its owner.

## License and responsibility

This repository is documentation and templates. Operators are responsible for their accounts, costs, permissions, platform terms, applicable law, and decisions made from outputs. See [SECURITY.md](SECURITY.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

<img width="1281" height="696" alt="Screenshot 2026-10-27 113151" src="https://github.com/user-attachments/assets/354cf730-6781-4df7-b6d3-96700ad03831" />

