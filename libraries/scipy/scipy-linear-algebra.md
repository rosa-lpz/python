# SciPy for Linear Algebra

The `scipy.linalg` module provides a **comprehensive set of linear algebra routines** that are more powerful and flexible than those in `numpy.linalg`. It builds on optimized libraries like LAPACK and BLAS under the hood.

------

## `scipy.linalg`

| Functionality            | Example Function                 | Description                                |
| ------------------------ | -------------------------------- | ------------------------------------------ |
| Solve linear systems     | `solve()`                        | Solve Ax = b                               |
| Matrix inversion         | `inv()`                          | Compute the inverse of a matrix            |
| Determinants             | `det()`                          | Compute matrix determinant                 |
| Matrix decompositions    | `lu()`, `qr()`, `svd()`, `eig()` | LU, QR, SVD, and eigenvalue decompositions |
| Matrix exponentials/logs | `expm()`, `logm()`               | Compute matrix exponentials, logarithms    |
| Norms                    | `norm()`                         | Matrix or vector norms                     |
| Pseudoinverse            | `pinv()`                         | Moore–Penrose pseudoinverse                |

------



## Examples

### 1. **Solving a linear system Ax = b**

```python
from scipy.linalg import solve
import numpy as np

A = np.array([[3, 2], [1, 4]])
b = np.array([5, 6])
x = solve(A, b)

print("Solution x:", x)
```

------

### 2. **Eigenvalues and Eigenvectors**

```python
from scipy.linalg import eig

A = np.array([[2, 0], [0, 3]])
w, v = eig(A)

print("Eigenvalues:", w)
print("Eigenvectors:\n", v)
```

------

### 3. **Singular Value Decomposition (SVD)**

```python
from scipy.linalg import svd

A = np.array([[1, 2], [3, 4], [5, 6]])
U, s, Vh = svd(A)

print("U matrix:\n", U)
print("Singular values:", s)
print("Vh matrix:\n", Vh)
```

------

### 4. **Matrix Exponential**

Useful in physics and chemistry (e.g., time evolution of quantum states):

```python
from scipy.linalg import expm

A = np.array([[0, 1], [-1, 0]])  # Rotation matrix generator
result = expm(A)

print("Matrix exponential expm(A):\n", result)
```

------





## `scipy.linalg` vs `numpy.linalg`

| Feature                 | `numpy.linalg` | `scipy.linalg`            |
| ----------------------- | -------------- | ------------------------- |
| Basic operations        | ✅              | ✅                         |
| Advanced decompositions | ❌              | ✅ (e.g., SVD, LU, Schur)  |
| Matrix functions        | ❌              | ✅ (`expm`, `logm`)        |
| Performance             | ⚠️              | ✅ (uses optimized LAPACK) |

Use `scipy.linalg` when:

- You need performance (large matrices)
- You're doing advanced decompositions or matrix functions
- You want more numerical stability or precision

------

Do you want help with a chemistry-related linear algebra problem (like molecular orbital theory or vibration analysis)? I’d be happy to show how `scipy.linalg` fits into that!
