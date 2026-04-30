from __future__ import annotations
from .exceptions import InvalidModError, InvalidModOperationError, InvalidTypeOperationError, InvalidInverseError
from functools import total_ordering

@total_ordering
class ModInt:
    def __init__(self, value: int, mod: int) -> None:
        if mod <= 1:
            raise InvalidModError(f"Modulus must be greater than 1, got {mod}")
        self.value = value % mod
        self.mod = mod

    def __str__(self) -> str:
        return f"({self.value} % {self.mod})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value!r}, mod={self.mod!r})"

    def _check_value(self, other: "ModInt" | int) -> int:
        if isinstance(other, ModInt):
            if self.mod != other.mod:
                raise InvalidModOperationError(f"Modulus must be the same, got {self.mod} and {other.mod}")
            return other.value
        elif isinstance(other, int):
            return other % self.mod
        raise InvalidTypeOperationError(f"Invalid value, got {type(other)}")

    def __add__(self, other: "ModInt" | int) -> "ModInt":
        value = self._check_value(other)
        return ModInt((self.value + value) % self.mod, self.mod)
    def __radd__(self, other: "ModInt" | int) -> "ModInt":
        return self.__add__(other)

    
    def __sub__(self, other: "ModInt" | int) -> "ModInt":
        value = self._check_value(other)
        return ModInt((self.value - value) % self.mod, self.mod)
    def __rsub__(self, other: "ModInt" | int) -> "ModInt":
        value = self._check_value(other)
        return ModInt((value - self.value) % self.mod, self.mod)

    def __mul__(self, other: "ModInt" | int) -> "ModInt":
        value = self._check_value(other)
        return ModInt((self.value * value) % self.mod, self.mod)
    def __rmul__(self, other: "ModInt" | int) -> "ModInt":
        return self.__mul__(other)

    def __neg__(self) -> "ModInt":
        return ModInt(-self.value % self.mod, self.mod)

    def __pow__(self, other: int) -> "ModInt":
        result = ModInt(1, self.mod)
        if other > 0:
            base = ModInt(self.value, self.mod)
        elif other < 0:
            base = self.inverse()
            other = -other
        while other > 0:
            if other % 2 == 1:
                result = result * base
            base = base * base
            other //= 2
        return result

    def inverse(self) -> "ModInt":
        bezout = self.egcd(self.value, self.mod)
        if bezout[0] != 1:
            raise InvalidInverseError(f"Value and modul must be coprime,got {self.value} and {self.mod}")
        return ModInt(bezout[1], self.mod)
        

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        Computes the greatest common divisor of a and b.
        Uses the highly efficient iterative Euclidean algorithm.
        """
        while b:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def egcd(a: int, b: int) -> tuple[int, int, int]:
        """
        Extended Euclidean Algorithm.
        Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
        Crucial for calculating modular inverses.
        """
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0
    
    def __truediv__(self, other: "ModInt" | int) -> "ModInt":
        val = self._check_value(other)
        return self * ModInt(val, self.mod).inverse()

    def __rtruediv__(self, other: int) -> "ModInt":
        return ModInt(other, self.mod) * self.inverse()

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ModInt):
            return (self.value == other.value) and (self.mod == other.mod)
        if isinstance(other, int):
            return self.value == (other % self.mod)
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.value, self.mod))


    def __lt__(self, other: "ModInt" | int) -> bool:
        value = self._check_value(other)
        return self.value < value
    
    def __int__(self) -> int:
        return self.value

    @staticmethod
    def totient(n: int) -> int:
        """
        Computes Euler's totient function phi(n).
        Counts the positive integers up to n that are relatively prime to n.
        Uses the optimal O(sqrt(n)) prime factorization algorithm.
        """
        if n <= 0:
            raise ValueError("totient function is only defined for positive integers")
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result