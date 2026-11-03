"""
Cutaneous Axon Reflex Flare & C-Fiber Neurogenic Vasodilation Engine.
Provides deterministic, zero-dependency modeling of Laser Doppler Perfusion Units (PU),
vasodilatory flare index (PU_peak / PU_base), flare radius (mm), and unmyelinated nociceptive C-fiber axonal integrity.
"""

from typing import Dict, Any, List, Optional


class CutaneousAxonReflexFlareClient:
    """
    Deterministic client for calculating Cutaneous Axon Reflex Vasodilation and Neurogenic Flare.
    Assesses unmyelinated polymodal C-nociceptive fiber branching, calcitonin gene-related peptide (CGRP) release,
    antidromic microvascular arborization, and small-fiber autonomic peripheral neuropathy.
    """

    def __init__(self):
        pass

    def evaluate_axon_reflex_flare(
        self,
        baseline_flux_pu: float,
        peak_flare_flux_pu: float,
        flare_radius_mm: float,
        stimulus_type: str = "HISTAMINE_IONTOPHORESIS"
    ) -> Dict[str, Any]:
        """
        Calculates Vasodilatory Index (VI = peak_flux / baseline_flux) and small-fiber flare score.
        Normative values (Laser Doppler Imaging / Histamine challenge):
        - Baseline Flux: 10.0 - 25.0 PU
        - Peak Flare Flux: 60.0 - 160.0 PU
        - Vasodilatory Index (VI): 3.5 - 7.5x
        - Flare Radius: 12.0 - 25.0 mm
        """
        if baseline_flux_pu <= 0 or peak_flare_flux_pu <= 0 or flare_radius_mm <= 0:
            return {"error": "Perfusion units and flare radius must be strictly positive"}
        if peak_flare_flux_pu <= baseline_flux_pu:
            return {"error": "Peak flare flux must exceed baseline perfusion flux"}

        # 1. Vasodilatory Flare Index (VI = PU_peak / PU_base)
        vi_ratio = round(peak_flare_flux_pu / baseline_flux_pu, 2)

        # 2. Total Flare Increase (PU)
        delta_flux_pu = round(peak_flare_flux_pu - baseline_flux_pu, 1)

        # 3. C-Fiber Neurogenic Flare Score (0 - 100)
        score = 80.0
        if 4.0 <= vi_ratio <= 7.5:
            score += 10.0
        elif 3.0 <= vi_ratio < 4.0:
            score += 5.0
        elif vi_ratio < 2.0:
            score -= 30.0  # Profound C-fiber axon reflex loss
        elif vi_ratio < 2.8:
            score -= 15.0

        if 13.0 <= flare_radius_mm <= 24.0:
            score += 10.0
        elif 10.0 <= flare_radius_mm < 13.0:
            score += 5.0
        elif flare_radius_mm < 7.0:
            score -= 25.0  # Restricted axonal collateral spread
        elif flare_radius_mm < 10.0:
            score -= 12.0

        flare_score = round(min(100.0, max(5.0, score)), 1)

        if flare_score >= 85.0 and vi_ratio >= 3.5 and flare_radius_mm >= 12.0:
            tier = "OPTIMAL_C_FIBER_AXON_REFLEX_FLARE"
            interp = f"Robust neurogenic axon reflex flare (VI {vi_ratio}x, Radius {flare_radius_mm} mm, Delta {delta_flux_pu} PU); brisk CGRP/substance P antidromic microvascular arborization."
            guidance = "Superior small-fiber nociceptive and neurovascular signaling. Intact unmyelinated epidermal nerve fiber density."
        elif vi_ratio < 2.4 or flare_radius_mm < 8.5:
            tier = "BLUNTED_AXON_REFLEX_SMALL_FIBER_DEFICIT"
            interp = f"Severely attenuated neurogenic flare (VI {vi_ratio}x < 3.0x, Radius {flare_radius_mm} mm < 10 mm); reflects sensory axonal dropout or small-fiber autonomic neuropathy."
            guidance = "Small-fiber axonal degeneration suspected. Screen for glycemic dysregulation, toxic microangiopathy, or B12/folate deficiency."
        else:
            tier = "MODERATE_AXONAL_FLARE_VASODILATION"
            interp = f"Moderate axon reflex flare response (VI {vi_ratio}x, Radius {flare_radius_mm} mm); preserved peripheral perfusion baseline."
            guidance = "Acceptable microvascular axon reflex. Maintain regular skin hydration and cardiovascular conditioning."

        return {
            "stimulus_type": stimulus_type,
            "baseline_flux_pu": baseline_flux_pu,
            "peak_flare_flux_pu": peak_flare_flux_pu,
            "delta_flux_pu": delta_flux_pu,
            "vasodilatory_index": vi_ratio,
            "flare_radius_mm": flare_radius_mm,
            "c_fiber_flare_score": flare_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
