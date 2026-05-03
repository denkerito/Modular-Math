# 🛡️ modMath: High-Performance Modular Arithmetic & Cryptographic Suite

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)
[![CI/CD Pipeline](https://github.com/yourusername/modMath/actions/workflows/pytest.yml/badge.svg)](https://github.com/yourusername/modMath/actions)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Poetry](https://img.shields.io/badge/Package%20Manager-Poetry-60A5FA.svg)](https://python-poetry.org/)

**modMath** is a sophisticated, production-ready Python library engineered for precision modular arithmetic, advanced number theory, and classical cryptographic operations. Built with a focus on **architectural elegance** and **mathematical rigor**, it bridges the gap between low-level algorithmic efficiency and high-level developer experience.

---

## 🚀 Key Engineering Highlights

*   **⚡ Elegant Core Architecture**: Leverages Python’s operator overloading to provide an intuitive, native-feeling API for modular integers (`ModInt`).
*   **🔐 Cryptographic Excellence**: Features a suite of optimized classical ciphers (Caesar, Affine, Vigenère) built on top of a robust modular engine.
*   **🧮 Advanced Number Theory**: Implements high-level algorithms including the **Chinese Remainder Theorem (CRT)** and the **Extended Euclidean Algorithm** for efficient modular inversions.
*   **🌐 Cloud-Ready API**: A fully-featured REST interface built with **FastAPI**, featuring automatic OpenAPI (Swagger) documentation and high-concurrency support.
*   **🛠️ Professional Tooling**: 100% test coverage via `pytest`, strictly managed dependencies via `Poetry`, and a robust **GitHub Actions CI/CD** pipeline for automated quality assurance.

---

## 🏗️ Architectural Overview

### 1. The Modular Engine (`ModInt`)
The heartbeat of the library. It isn't just a wrapper; it's a full mathematical implementation of $\mathbb{Z}/n\mathbb{Z}$ rings.

```python
from modMath import ModInt

# Seamless operator overloading for native-feel arithmetic
a, b = ModInt(5, 7), ModInt(4, 7)

print(a + b)  # (2 % 7)
print(a / b)  # (3 % 7) - Leverages Extended Euclidean Algorithm for modular inverse
print(a ** -1) # (2 % 7) - Native support for negative exponents
```

### 2. Cryptographic Implementations
Engineered with modularity in mind, allowing for easy expansion into modern public-key systems (RSA/ECC).

```python
from modMath import VigenereCipher, AffineCipher

# Polyalphabetic substitution with automated index management
vigenere = VigenereCipher(keyword="CRYPTO")
print(vigenere.encrypt("SCALABLE ARCHITECTURE")) 

# Linear transformation cipher E(x) = (ax + b) mod m
affine = AffineCipher(a=5, b=8)
print(affine.encrypt("PRODUCTION"))
```

### 3. Number Theory Suite
Solving complex systems of congruences with high-efficiency algorithms.

```python
from modMath import chinese_remainder_theorem

# Solve: x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)
# x = 23 (mod 105)
print(chinese_remainder_theorem([2, 3, 2], [3, 5, 7]))
```

---

## 🌍 REST API: Math-as-a-Service

modMath is ready for the cloud. Deploy the FastAPI service to expose mathematical operations to any frontend or external service.

```bash
# Spin up the production-grade server
poetry run uvicorn api.main:app --host 0.0.0.0 --port 8000
```

**Featured Endpoints:**
- `POST /crypto/vigenere/encrypt`: Industrial-grade polyalphabetic encryption.
- `POST /op/crt`: High-speed congruence system solver.
- `POST /op/inverse`: Instant modular multiplicative inverse calculation.

---

## 🛠️ Installation & Development

This project adheres to modern Python packaging standards using **Poetry**.

```bash
# Clone the enterprise-ready codebase
git clone https://github.com/yourusername/modMath.git
cd modMath

# Initialize the hermetic virtual environment
poetry install
```

### Quality Assurance
Our CI/CD pipeline ensures every commit meets strict stability standards.
```bash
# Run the exhaustive 57-test suite
$env:PYTHONPATH="."
poetry run pytest
```

---

## 📜 License & Contribution

Engineered with ❤️ by **Dennis**. 

*This project is part of a professional portfolio demonstrating expertise in algorithmic design, Pythonic software architecture, and RESTful service integration.*
