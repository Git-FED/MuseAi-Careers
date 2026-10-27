# VM and worker operations

This document describes a measured test environment, not a promise that a swarm is profitable.

## Baseline

The brief references shared 2-vCPU VMs, frequent restarts, and competing agent lanes. Record actual provider, region, CPU, RAM, storage, hourly cost, restart history, and workload before estimating yield.

## Safe worker pattern

- Use a supervised service with explicit resource limits.
- Reserve capacity for monitoring and shutdown.
- Emit heartbeats and stop on repeated failures.
- Use provider-supported uptime and scheduling features; do not bypass sleep controls or quotas.
- Reconcile total compute cost against measured output daily.

No miner is installed by this repository. Deployment requires explicit authorization, a compliant provider/pool, and a documented cost gate.
