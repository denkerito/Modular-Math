from __future__ import annotations
from .Exceptions import InvalidModError, InvalidModOperationError, InvalidTypeOperationError, InvalidInverseError

class Mod_int:
    def __init__(self, value: int, mod: int) -> None:
        if mod <= 1:
            raise InvalidModError(f"Modulus must be greater than 1, got {mod}")
        self.value = value % mod
        self.mod = mod

    def __str__(self) -> str:
        return f"({self.value} % {self.mod})"

    def _check_value(self, other: "Mod_int" | int) -> int:
        if isinstance(other, Mod_int):
            if self.mod != other.mod:
                raise InvalidModOperationError(f"Modulus must be the same, got {self.mod} and {other.mod}")
            return other.value
        elif isinstance(other, int):
            return other % self.mod
        raise InvalidTypeOperationError(f"Invalid value, got {type(other)}")

    def __add__(self, other: "Mod_int" | int) -> "Mod_int":
        value = self._check_value(other)
        return Mod_int((self.value + value) % self.mod, self.mod)
    def __radd__(self, other: "Mod_int" | int) -> "Mod_int":
        return self.__add__(other)

    
    def __sub__(self, other: "Mod_int" | int) -> "Mod_int":
        value = self._check_value(other)
        return Mod_int((self.value - value) % self.mod, self.mod)
    def __rsub__(self, other: "Mod_int" | int) -> "Mod_int":
        value = self._check_value(other)
        return Mod_int((value - self.value) % self.mod, self.mod)

    def __mul__(self, other: "Mod_int" | int) -> "Mod_int":
        value = self._check_value(other)
        return Mod_int((self.value * value) % self.mod, self.mod)
    def __rmul__(self, other: "Mod_int" | int) -> "Mod_int":
        return self.__mul__(other)

    def __neg__(self) -> "Mod_int":
        return Mod_int(-self.value % self.mod, self.mod)

    def __pow__(self, other: int) -> "Mod_int":
        result = Mod_int(1, self.mod)
        if other > 0:
            base = Mod_int(self.value, self.mod)
        elif other < 0:
            base = self.inverse()
            other = -other
        while other > 0:
            if other % 2 == 1:
                result = result * base
            base = base * base
            other //= 2
        return result

    def inverse(self) -> "Mod_int":
        bezout = self.egcd(self.value, self.mod)
        if bezout[0] != 1:
            raise InvalidInverseError(f"Value and modul must be coprime,got {self.value} and {self.mod}")
        return Mod_int(bezout[1], self.mod)
        

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
    
    def __truediv__(self, other: "Mod_int" | int) -> "Mod_int":
        value = Mod_int(self._check_value(other), other.mod)
        return Mod_int(self.value * value.inverse(), self.mod)

    def __rtruediv__(self, other: int) -> "Mod_int":
        return Mod_int(other, self.mod) * self.inverse()