# ADR-0003: AI Sentinel Governance System

| Field | Value |
|-------|-------|
| Status | Accepted |
| Date | 2026-06-26 |
| Confidence | High |

## Context
AI-assisted development introduces risks: hallucinated APIs, undocumented changes, architectural drift.

## Decision
Install AI Sentinel as permanent governance, bound by SENTINEL.md.

## Reason
- Verifies references before use
- Requires documentation updates with every change
- Enforces human approval gates for high-risk actions

## Alternatives Considered
No governance - rejected (high hallucination risk).

## Consequences
Positive: Systematic quality control, decision history.
Negative: Overhead per task.

## References
- SENTINEL.md