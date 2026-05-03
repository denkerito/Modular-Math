from modMath import ModInt
from functools import reduce
import operator

def chinese_remainder_theorem(remainders: list[int], moduli: list[int]) -> int:
    """
    Solves a system of simultaneous congruences using the Chinese Remainder Theorem.
    
    Given remainders a_i and moduli m_i, finds x such that:
    x ≡ a_i (mod m_i) for all i.
    
    The moduli must be pairwise coprime.
    """
    if len(remainders) != len(moduli):
        raise ValueError("Remainders and moduli lists must have the same length")
    if not moduli:
        raise ValueError("Moduli list cannot be empty")
        
    # Check if moduli are pairwise coprime
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if ModInt.gcd(moduli[i], moduli[j]) != 1:
                raise ValueError(f"Moduli must be pairwise coprime, but gcd({moduli[i]}, {moduli[j]}) != 1")

    total_modulus = reduce(operator.mul, moduli, 1)
    result = 0
    
    for a_i, m_i in zip(remainders, moduli):
        M_i = total_modulus // m_i
        # Calculate modular inverse of M_i modulo m_i
        y_i = ModInt(M_i, m_i).inverse().value
        result += a_i * M_i * y_i
        
    return result % total_modulus
