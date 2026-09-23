"""Estimate the standard Gibbs energy for ammonia formation at 298.15 K.

This is a thermochemical table calculation, not an ORCA/MAESTRO result.
"""

TEMPERATURE_K = 298.15
PRESSURE_MPA = 0.1

# NIST-JANAF standard Gibbs energies of formation at 298.15 K (kJ/mol).
# Elements in their standard states have Delta_f G degree = 0.
GIBBS_FORMATION_KJ_MOL = {
    "N2(g)": 0.0,
    "H2(g)": 0.0,
    "NH3(g)": -16.367,
}

STOICHIOMETRY = {
    "N2(g)": -1,
    "H2(g)": -3,
    "NH3(g)": 2,
}


def main() -> None:
    contributions = {
        species: STOICHIOMETRY[species] * gibbs
        for species, gibbs in GIBBS_FORMATION_KJ_MOL.items()
    }
    reaction_gibbs = sum(contributions.values())

    print(f"T = {TEMPERATURE_K:.2f} K")
    print(f"p standard = {PRESSURE_MPA:.1f} MPa")
    print("Reaction: N2(g) + 3 H2(g) -> 2 NH3(g)")
    for species, contribution in contributions.items():
        print(f"  {species}: {contribution:.3f} kJ/mol-reaction")
    print(f"Delta_r G degree = {reaction_gibbs:.3f} kJ/mol-reaction")
    print(f"Per mole NH3 = {reaction_gibbs / 2:.3f} kJ/mol-NH3")


if __name__ == "__main__":
    main()
