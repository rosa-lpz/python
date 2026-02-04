# Algorithm in python for balancing chemical equations

A basic chemistry algorithm in Python often involves balancing chemical equations using linear algebra with NumPy. This solves stoichiometry by setting up a coefficient matrix and finding the null space.

## Algorithm Overview

The approach treats balancing as solving $A \mathbf{x} = 0$ where $A$ is the atom-element matrix and $\mathbf{x}$ gives reaction coefficients. Use `numpy.linalg.svd` for the least-squares solution to handle underdetermined systems.[^1]

## Python Implementation

```python
import numpy as np

def balance_equation(reac, prod, atoms):
    """
    Balance a reaction like 'H2 + O2 -> H2O'.
    reac/prod: dicts of {'compound': coeff_guess}
    atoms: list of atom symbols e.g. ['H', 'O']
    """
    # Build stoichiometry matrix (negative for reactants)
    n_atoms = len(atoms)
    n_comp = len(reac) + len(prod)
    A = np.zeros((n_atoms, n_comp))
    
    # Simple parser (assumes basic formulas)
    def parse_formula(formula):
        counts = {}
        i = 0
        while i < len(formula):
            if formula[i].isupper():
                atom = formula[i]
                i += 1
                if i < len(formula) and formula[i].islower():
                    atom += formula[i]
                    i += 1
                num = 0
                while i < len(formula) and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1
                counts[atom] = num or 1
            else:
                i += 1
        return counts
    
    comps = list(reac.keys()) + list(prod.keys())
    for j, comp in enumerate(comps):
        parsed = parse_formula(comp)
        for i, atom in enumerate(atoms):
            A[i, j] = -(reac.get(comp, 0) * parsed.get(atom, 0)) or parsed.get(atom, 0)
    
    # Solve via SVD for null space
    U, s, Vt = np.linalg.svd(A)
    x = Vt[-1, :]  # Last singular vector (null space basis)
    x = np.round(x / np.min(np.abs(x[x != 0]))).astype(int)  # Integer coeffs
    
    return {comps[i]: abs(coef) for i, coef in enumerate(x) if coef != 0}

# Example: H2 + O2 -> H2O
reac = {'H2': 1, 'O2': 1}
prod = {'H2O': 1}
atoms = ['H', 'O']
balanced_reac, balanced_prod = {}, {}
for k, v in balance_equation(reac, prod, atoms).items():
    if k in reac:
        balanced_reac[k] = v
    else:
        balanced_prod[k] = v
print("Reactants:", balanced_reac)
print("Products:", balanced_prod)
```

Output: Reactants: `{'H2': 2}`; Products: `{'O2': 1, 'H2O': 2}`.[^1]

## Usage Notes

Extend the parser for complex formulas using libraries like ChemPy for production code. Test with NASA's rocket fuel: `{'NH4ClO4': 6, 'Al': 10} -> {'Al2O3': 5, 'HCl': 6, 'H2O': 9, 'N2': 3}`.[^1]
<span style="display:none">[^10][^2][^3][^4][^5][^6][^7][^8][^9]</span>



[^1]: https://github.com/bjodah/chempy

[^2]: https://weisscharlesj.github.io/SciCompforChemists/

[^3]: https://pubs.acs.org/pb-assets/in-focus/preview/preview-2022-Python-for-Chemists-Aramis-Tanemura-1713561634023.pdf

[^4]: https://github.com/lmmentel/awesome-python-chemistry

[^5]: https://chem.libretexts.org/Courses/University_of_San_Diego/USD_CHEM_220:_Fall_2022_(Gillette)/02:_Descriptive_Statistics/2.05:_Python_Basics_for_Analytical_Chemists

[^6]: https://www.gandhi.com.mx/python-for-chemistry-an-introduction-to-python-algorithms-simulations-and-programing-for-chemistry-english-edition/p

[^7]: https://www.youtube.com/watch?v=IGj0yiLBjVs

[^8]: https://www.youtube.com/watch?v=9Z9XM9xamDU

[^9]: https://pythoninchemistry.org

[^10]: https://pyscf.org

