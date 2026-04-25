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
            base = Mod_int(1, self.mod) # Inverse of base, i still need to implement this
        while other > 0:
            if other % 2 == 1:
                result = result * base
            base = base * base
            other //= 2
        return result
    
    