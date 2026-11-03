# Cutaneous Axon Reflex Flare (Laser Doppler) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Cutaneous Axon Reflex Vasodilatory Index (PU_peak/PU_base), flare radius (mm), and unmyelinated nociceptive C-fiber axonal integrity.

```mermaid
flowchart TD
    NociceptiveStim["Localized Cutaneous Stimulation (Histamine / Electrical)"] --> Orthodromic["Orthodromic Sensory Action Potentials (To Spinal Cord)"]
    NociceptiveStim --> Antidromic["Antidromic Collateral Branching into Dermal Arterioles"]
    Antidromic --> NeuropeptideRelease["Substance P & CGRP Neuropeptide Secretion"]
    NeuropeptideRelease --> NeurogenicFlare["Widespread Arteriolar Vasodilation Flare (Laser Doppler Flux)"]
    NeurogenicFlare --> FlareEngine["Vasodilatory Flare Index (VI) & C-Fiber Integrity Score"]
    FlareEngine --> Agent["OpenClaw / Hermes Personal Agent Neuropathy Screening"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Neurovascular Autonomic Standards**: Implements validated equations for Laser Doppler flux, Vasodilatory Index, and flare radius spread.
- **Small-Fiber Neuropathy Detection**: Highly sensitive detection of unmyelinated epidermal nerve fiber loss prior to standard nerve conduction studies.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CutaneousAxonReflexFlareClient

client = CutaneousAxonReflexFlareClient()
result = client.evaluate_axon_reflex_flare(
    baseline_flux_pu=14.5,
    peak_flare_flux_pu=88.0,
    flare_radius_mm=19.5
)
print("Vasodilatory Index:", result["vasodilatory_index"], "x")
print("C-Fiber Score:", result["c_fiber_flare_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
