# Ammonia formation: standard Gibbs energy estimate

## Scope

This is a table-based thermodynamic calculation, not an ORCA or MAESTRO
quantum-chemistry result. No quantum-chemistry job was submitted.

Reaction:

```text
N2(g) + 3 H2(g) -> 2 NH3(g)
```

Conditions: 298.15 K and standard-state pressure 0.1 MPa (1 bar).

## Input data

The NIST-JANAF table gives the standard Gibbs energy of formation of NH3(g)
at 298.15 K as -16.367 kJ/mol. N2(g) and H2(g), as elements in their standard
states, each have a standard Gibbs energy of formation of 0 kJ/mol.

Source: [NIST-JANAF ammonia table](https://janaf.nist.gov/tables/H-083.html)

## Calculation

The standard reaction Gibbs energy is calculated from stoichiometric
coefficients `nu_i`:

```text
Delta_r G degree = sum(nu_i * Delta_f G_i degree)
                 = 2*(-16.367) - 1*(0) - 3*(0)
                 = -32.734 kJ/mol-reaction
```

Therefore, the value per mole of ammonia formed is:

```text
-32.734 / 2 = -16.367 kJ/mol-NH3
```

The negative sign means ammonia formation is thermodynamically favorable
under standard-state conditions at 298.15 K. It does not describe the kinetic
barrier or the industrial reaction rate.

## Reproduce

Run:

```bash
python3 calculate_standard_gibbs.py
```

Expected result:

```text
Delta_r G degree = -32.734 kJ/mol-reaction
Per mole NH3 = -16.367 kJ/mol-NH3
```
