import pytest
from modMath import chinese_remainder_theorem

def test_crt_basic():
    # x ≡ 2 (mod 3)
    # x ≡ 3 (mod 5)
    # x ≡ 2 (mod 7)
    # Solution: x = 23 (mod 105)
    assert chinese_remainder_theorem([2, 3, 2], [3, 5, 7]) == 23

def test_crt_another():
    # x ≡ 0 (mod 3)
    # x ≡ 3 (mod 4)
    # x ≡ 4 (mod 5)
    # Solution: x = 39 (mod 60)
    assert chinese_remainder_theorem([0, 3, 4], [3, 4, 5]) == 39

def test_crt_mismatched_lengths():
    with pytest.raises(ValueError, match="same length"):
        chinese_remainder_theorem([1, 2], [3, 4, 5])

def test_crt_non_coprime_moduli():
    with pytest.raises(ValueError, match="pairwise coprime"):
        chinese_remainder_theorem([1, 2], [10, 20])

def test_crt_empty_input():
    with pytest.raises(ValueError, match="cannot be empty"):
        chinese_remainder_theorem([], [])
