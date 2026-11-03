---
name: genpark-personal-agent-cutaneous-axon-reflex-flare-laser-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Cutaneous Axon Reflex Vasodilatory Index (PU_peak/PU_base), flare radius (mm), and unmyelinated nociceptive C-fiber axonal integrity.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cutaneous Axon Reflex Flare (Laser Doppler) Skill

A sovereign personal agent capability for evaluating unmyelinated polymodal C-nociceptive fiber branching, antidromic vasodilatory flare spread, calcitonin gene-related peptide (CGRP) release, and small-fiber autonomic neuropathy.

## Core Capabilities
- **Laser Doppler Perfusion Unit (PU) Profiling**: Tracks cutaneous microvascular baseline and post-stimulation peak blood flow.
- **Vasodilatory Flare Index (VI)**: Calculates the amplification ratio ($VI = PU_{peak} / PU_{baseline}$, normative: $3.5 - 7.5\times$).
- **Antidromic Flare Radius Measurement**: Quantifies axonal arborization spread radius in millimeters ($12.0 - 25.0\text{ mm}$).
- **Small-Fiber Neuropathy Screening**: Identifies early epidermal axonal degeneration before large myelinated fiber conduction loss.

## Fast Invocation
```python
from client import CutaneousAxonReflexFlareClient

client = CutaneousAxonReflexFlareClient()
res = client.evaluate_axon_reflex_flare(
    baseline_flux_pu=14.5,
    peak_flare_flux_pu=88.0,
    flare_radius_mm=19.5
)
print("Vasodilatory Index:", res["vasodilatory_index"], "x")
print("C-Fiber Score:", res["c_fiber_flare_score"], "/ 100")
```
