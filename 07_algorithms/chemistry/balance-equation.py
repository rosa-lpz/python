
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