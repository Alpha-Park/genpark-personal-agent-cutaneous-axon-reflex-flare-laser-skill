"""
Example Usage: Cutaneous Axon Reflex Flare & C-Fiber Neurogenic Vasodilation.
Demonstrates zero-dependency calculation of Laser Doppler flare flux, Vasodilatory Index, and small-fiber scoring.
"""

from client import CutaneousAxonReflexFlareClient


def main():
    client = CutaneousAxonReflexFlareClient()
    print("=== Cutaneous Axon Reflex Flare Demo ===")

    # Test Case 1: Healthy vigorous neurogenic axon reflex flare (Forearm)
    res1 = client.evaluate_axon_reflex_flare(
        baseline_flux_pu=14.5,
        peak_flare_flux_pu=88.0,
        flare_radius_mm=19.5,
        stimulus_type="HISTAMINE_IONTOPHORESIS"
    )
    print("\nTest Case 1: Robust Axon Reflex Neurogenic Flare")
    print(f"  Baseline Flux: {res1['baseline_flux_pu']} PU | Peak Flux: {res1['peak_flare_flux_pu']} PU (Delta: {res1['delta_flux_pu']} PU)")
    print(f"  Vasodilatory Index (VI): {res1['vasodilatory_index']}x | Flare Radius: {res1['flare_radius_mm']} mm")
    print(f"  C-Fiber Flare Score: {res1['c_fiber_flare_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Blunted axon reflex flare (small fiber neuropathy pattern)
    res2 = client.evaluate_axon_reflex_flare(
        baseline_flux_pu=12.0,
        peak_flare_flux_pu=24.5,
        flare_radius_mm=6.8,
        stimulus_type="HISTAMINE_IONTOPHORESIS"
    )
    print("\nTest Case 2: Small-Fiber Axon Reflex Deficit Pattern")
    print(f"  Vasodilatory Index: {res2['vasodilatory_index']}x | Flare Radius: {res2['flare_radius_mm']} mm")
    print(f"  C-Fiber Flare Score: {res2['c_fiber_flare_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
