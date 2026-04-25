# modMath

A lightweight and efficient Python library for modular arithmetic, designed for ease of use and mathematical correctness.

## Features

- **Modular Integers**: Perform arithmetic operations on integers within a specific modulus.
- **Full Operator Support**: Supports `+`, `-`, `*`, `/`, `**` (including negative exponents), and unary `-`.
- **Automatic Reduction**: All operations automatically reduce the result modulo $N$.
- **Modular Inverse**: Calculate modular multiplicative inverses using the Extended Euclidean Algorithm.
- **Comparison Operators**: Supports standard comparisons (`==`, `<`, `>`, etc.) between `ModInt` objects and integers.
- **Hashing**: `ModInt` objects are hashable and can be used as dictionary keys or in sets.
- **Type Safety**: Includes custom exceptions for invalid modulus, mismatched moduli in operations, and non-invertible values.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

```bash
# Clone the repository
git clone https://github.com/yourusername/modMath.git
cd modMath

# Install dependencies
poetry install
```

## Usage

### Basic Arithmetic

```python
from modMath import ModInt

# Initialize a ModInt (value=5, mod=7)
a = ModInt(5, 7)
b = ModInt(4, 7)

# Addition
print(a + b)  # Output: (2 % 7)

# Subtraction
print(a - b)  # Output: (1 % 7)

# Multiplication
print(a * b)  # Output: (6 % 7)

# Division (modular inverse)
print(a / b)  # Output: (3 % 7)
```

### Powers and Inverses

```python
from modMath import ModInt

a = ModInt(5, 7)

# Power
print(a ** 3)  # Output: (6 % 7)

# Negative exponent (Modular Inverse)
print(a ** -1) # Output: (3 % 7)

# Explicit Modular Inverse
print(a.inverse()) # Output: (3 % 7)
```

### Utilities

```python
from modMath import ModInt

# GCD
print(ModInt.gcd(48, 18)) # Output: 6

# Extended GCD (returns g, x, y such that ax + by = g)
g, x, y = ModInt.egcd(48, 18)
print(f"gcd: {g}, x: {x}, y: {y}") # Output: gcd: 6, x: -1, y: 3
```

## Exceptions

The library defines several custom exceptions in `modMath.exceptions`:

- `InvalidModError`: Raised when initializing with a modulus ≤ 1.
- `InvalidModOperationError`: Raised when performing operations between `ModInt` objects with different moduli.
- `InvalidTypeOperationError`: Raised when performing operations with unsupported types.
- `InvalidInverseError`: Raised when a modular inverse does not exist (i.e., $\gcd(\text{value}, \text{mod}) \neq 1$).

## Running Tests

Tests are written using `pytest`.

```bash
poetry run pytest
```

## License

This project is currently unlicensed.
