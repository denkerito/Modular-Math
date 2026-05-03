# modMath

A lightweight and efficient Python library for modular arithmetic and classical cryptography, designed for ease of use and mathematical correctness.

## Features

- **Modular Integers**: Perform arithmetic operations on integers within a specific modulus.
- **Full Operator Support**: Supports `+`, `-`, `*`, `/`, `**` (including negative exponents), and unary `-`.
- **Cryptography Module**:
  - **Caesar Cipher**: Standard shift substitution.
  - **Affine Cipher**: Linear substitution ($ax + b \pmod m$).
  - **Vigenère Cipher**: Polyalphabetic substitution using a keyword.
- **Number Theory Tools**:
  - **Chinese Remainder Theorem (CRT)**: Solve systems of simultaneous congruences.
  - **Extended Euclidean Algorithm**: Efficient calculation of GCD and Bézout coefficients.
- **REST API**: A complete web service built with FastAPI to perform modular operations and encryption/decryption via HTTP.
- **Type Safety**: Robust error handling with custom exceptions for mathematical edge cases.

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

# Addition: (5 + 4) % 7 = 2
print(a + b)  # Output: (2 % 7)

# Division (modular inverse): 5 * 4⁻¹ % 7 = 5 * 2 % 7 = 3
print(a / b)  # Output: (3 % 7)
```

### Cryptography

```python
from modMath import VigenereCipher, AffineCipher

# Vigenère Cipher
cipher = VigenereCipher(keyword="KEY")
encrypted = cipher.encrypt("HELLO WORLD")
print(encrypted) # Output: "RIJVS GAVPH"

# Affine Cipher (E(x) = (5x + 8) mod 26)
affine = AffineCipher(a=5, b=8)
print(affine.encrypt("ABC")) # Output: "INS"
```

### Number Theory (CRT)

```python
from modMath import chinese_remainder_theorem

# Solve: x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)
result = chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
print(result) # Output: 23
```

## API Web Service

modMath includes a FastAPI-based REST API.

### Starting the API
```bash
poetry run uvicorn api.main:app --reload
```
Once started, you can access the interactive documentation at `http://127.0.0.1:8000/docs`.

### Sample API Request (Vigenère Encryption)
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/crypto/vigenere/encrypt' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "HELLO",
  "keyword": "KEY"
}'
```

## Running Tests

Tests are written using `pytest`.

```bash
# Set PYTHONPATH to include project root for API tests
$env:PYTHONPATH="."
poetry run pytest
```

## License

This project is currently unlicensed.
