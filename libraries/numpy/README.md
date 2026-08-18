# NumPy

**NumPy** (Numerical Python) is the foundational library for scientific computing in Python. It provides a powerful N-dimensional array object, tools for integrating C/C++, and highly optimized functions for linear algebra, Fourier transforms, and random numbers.

Here is a comprehensive summary of how it works and its core functionality.

---

## The Core Concept: The `ndarray`

At the heart of NumPy is the **`ndarray`** (N-dimensional array). Unlike standard Python lists, which can hold different data types and are scattered in memory, NumPy arrays are **homogenous** (all elements must be the same type) and stored in **contiguous memory blocks**.

This architectural difference allows NumPy to perform operations via **vectorization**—eliminating the need for explicit `for` loops in Python and running at C-speed.

---

## Key Operations & Cheat Sheet

### Array Creation

```python
import numpy as np

# From a Python list
a = np.array([1, 2, 3])

# Placeholders
zeros = np.zeros((2, 3))       # 2x3 array of zeros
ones = np.ones((3, 3))         # 3x3 array of ones
empty = np.empty((2, 2))       # Uninitialized array

# Sequences
arrange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5) # 5 evenly spaced numbers between 0 and 1

```

### Inspecting Properties

If `a` is an array:

* `a.shape`: Returns a tuple representing the array's dimensions (e.g., `(3, 4)`).
* `a.ndim`: Number of array dimensions (axes).
* `a.dtype`: Data type of the elements (e.g., `int32`, `float64`).
* `a.size`: Total number of elements in the array.

### Reshaping and Transposing

* `a.reshape(3, 2)`: Changes dimensions without changing data.
* `a.T` or `a.transpose()`: Flips the axes (rows become columns).
* `a.flatten()`: Collapses a multi-dimensional array into 1D.

---

## Advanced Mechanics: Indexing & Broadcasting

### Indexing and Slicing

NumPy extends standard Python slicing into multiple dimensions:
`array[row_slice, column_slice]`

```python
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

print(matrix[0, 1])    # Output: 2 (row 0, col 1)
print(matrix[:, 1])    # Output: [2, 5, 8] (all rows, col 1)
print(matrix[0:2, :])  # First two rows, all columns

```

### Broadcasting

Broadcasting allows mathematical operations on arrays of **different shapes**, provided they meet specific dimension compatibility rules. Instead of copying data, NumPy virtually stretches the smaller array to match the larger one.

```python
# Broadcasting example: adding a scalar to a 1D array
a = np.array([1, 2, 3])
print(a + 5) # Output: [6, 7, 8]

```

---

## Mathematical & Statistical Functions

NumPy includes highly optimized **universal functions** (`ufuncs`) that perform element-wise operations.

| Category | Functions | Example |
| --- | --- | --- |
| **Element-wise Math** | `np.sin()`, `np.cos()`, `np.exp()`, `np.log()`, `np.sqrt()` | `np.sqrt(a)` |
| **Reductions** | `np.sum()`, `np.mean()`, `np.median()`, `np.std()`, `np.min()`, `np.max()` | `matrix.sum(axis=0)` (column sums) |
| **Linear Algebra** | `np.dot()` (or `@`), `np.linalg.inv()`, `np.linalg.eig()` | `A @ B` (Matrix multiplication) |
| **Random Number** | `np.random.rand()`, `np.random.randn()`, `np.random.randint()` | `np.random.normal(0, 1, 100)` |

---

## Why use NumPy?

> **Speed:** Operations are implemented in compiled C code.
> **Memory Efficiency:** Uses far less memory than native Python lists of lists.
> **Ecosystem Foundation:** It serves as the bedrock for almost all Python data science libraries, including **Pandas, SciPy, Scikit-Learn, TensorFlow, and PyTorch**.

