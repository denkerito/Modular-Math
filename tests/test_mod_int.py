import pytest
from src.modMath.mod_int import ModInt
from src.modMath.exceptions import (
    InvalidModError,
    InvalidModOperationError,
    InvalidTypeOperationError,
    InvalidInverseError,
)

def test_init_valid():
    m = ModInt(5, 7)
    assert m.value == 5
    assert m.mod == 7
    m = ModInt(10, 7)
    assert m.value == 3
    assert m.mod == 7
    m = ModInt(-2, 7)
    assert m.value == 5
    assert m.mod == 7

def test_init_invalid_mod():
    with pytest.raises(InvalidModError):
        ModInt(5, 1)
    with pytest.raises(InvalidModError):
        ModInt(5, 0)
    with pytest.raises(InvalidModError):
        ModInt(5, -1)

def test_str():
    m = ModInt(5, 7)
    assert str(m) == "(5 % 7)"

def test_check_value_valid():
    m1 = ModInt(5, 7)
    m2 = ModInt(3, 7)
    assert m1._check_value(m2) == 3
    assert m1._check_value(10) == 3

def test_check_value_invalid_mod():
    m1 = ModInt(5, 7)
    m2 = ModInt(3, 8)
    with pytest.raises(InvalidModOperationError):
        m1._check_value(m2)

def test_check_value_invalid_type():
    m = ModInt(5, 7)
    with pytest.raises(InvalidTypeOperationError):
        m._check_value("string")
    with pytest.raises(InvalidTypeOperationError):
        m._check_value(3.5)

def test_add():
    m1 = ModInt(5, 7)
    m2 = ModInt(4, 7)
    res = m1 + m2
    assert res.value == 2
    assert res.mod == 7
    res = m1 + 10
    assert res.value == 1
    assert res.mod == 7

def test_radd():
    m = ModInt(5, 7)
    res = 10 + m
    assert res.value == 1
    assert res.mod == 7

def test_sub():
    m1 = ModInt(2, 7)
    m2 = ModInt(5, 7)
    res = m1 - m2
    assert res.value == 4
    assert res.mod == 7
    res = m1 - 10
    assert res.value == 6
    assert res.mod == 7

def test_rsub():
    m = ModInt(2, 7)
    res = 10 - m
    assert res.value == 1
    assert res.mod == 7
    res = 1 - m
    assert res.value == 6
    assert res.mod == 7

def test_mul():
    m1 = ModInt(5, 7)
    m2 = ModInt(4, 7)
    res = m1 * m2
    assert res.value == 6
    assert res.mod == 7
    res = m1 * 3
    assert res.value == 1
    assert res.mod == 7

def test_rmul():
    m = ModInt(5, 7)
    res = 3 * m
    assert res.value == 1
    assert res.mod == 7

def test_neg():
    m = ModInt(5, 7)
    res = -m
    assert res.value == 2
    assert res.mod == 7
    m2 = ModInt(0, 7)
    assert (-m2).value == 0

def test_pow_positive():
    m = ModInt(2, 7)
    res = m ** 3
    assert res.value == 1
    assert res.mod == 7

def test_pow_zero():
    m = ModInt(2, 7)
    res = m ** 0
    assert res.value == 1
    assert res.mod == 7

def test_pow_negative():
    m = ModInt(2, 7)
    res = m ** -1
    assert res.value == 4
    assert res.mod == 7
    res = m ** -2
    assert res.value == 2
    assert res.mod == 7

def test_inverse_valid():
    m = ModInt(2, 7)
    res = m.inverse()
    assert res.value == 4
    assert res.mod == 7

    m2 = ModInt(3, 11)
    res2 = m2.inverse()
    assert res2.value == 4
    assert res2.mod == 11

def test_inverse_invalid():
    m = ModInt(2, 8)
    with pytest.raises(InvalidInverseError):
        m.inverse()

def test_gcd():
    assert ModInt.gcd(48, 18) == 6
    assert ModInt.gcd(101, 103) == 1
    assert ModInt.gcd(-48, 18) == 6
    assert ModInt.gcd(0, 5) == 5

def test_egcd():
    g, x, y = ModInt.egcd(48, 18)
    assert g == 6
    assert 48 * x + 18 * y == 6

    g, x, y = ModInt.egcd(101, 10)
    assert g == 1
    assert 101 * x + 10 * y == 1

def test_truediv():
    m1 = ModInt(6, 7)
    m2 = ModInt(2, 7)
    res = m1 / m2
    assert res.value == 3
    assert res.mod == 7
    
    m3 = ModInt(3, 7)
    res = m1 / m3
    assert res.value == 2
    assert res.mod == 7

def test_truediv_int():
    m1 = ModInt(6, 7)
    res = m1 / 2
    assert res.value == 3
    assert res.mod == 7
    
    res = m1 / 3
    assert res.value == 2
    assert res.mod == 7

def test_rtruediv_int():
    m = ModInt(2, 7)
    res = 6 / m
    assert res.value == 3
    assert res.mod == 7

def test_truediv_invalid():
    m1 = ModInt(6, 8)
    m2 = ModInt(2, 8)
    with pytest.raises(InvalidInverseError):
        m1 / m2
    
    with pytest.raises(InvalidInverseError):
        m1 / 2

def test_equality():
    m1 = ModInt(5, 7)
    m2 = ModInt(5, 7)
    m3 = ModInt(3, 7)
    m4 = ModInt(5, 8)
    
    assert m1 == m2
    assert m1 != m3
    assert m1 != m4
    assert m1 != "string"

def test_hash():
    m1 = ModInt(5, 7)
    m2 = ModInt(5, 7)
    m3 = ModInt(3, 7)
    
    assert hash(m1) == hash(m2)
    assert hash(m1) != hash(m3)
    
    # Test as dictionary key
    d = {m1: "value"}
    assert d[m2] == "value"

def test_comparison():
    m1 = ModInt(2, 7)
    m2 = ModInt(5, 7)
    m3 = ModInt(2, 7)
    
    assert m1 < m2
    assert m1 <= m2
    assert m1 <= m3
    assert m2 > m1
    assert m2 >= m1
    assert m1 >= m3
    
    # Test with int
    assert m1 < 5
    assert m1 <= 5
    assert m1 <= 2
    assert m2 > 2
    assert m2 >= 2
    assert m1 >= 2

def test_comparison_invalid_mod():
    m1 = ModInt(2, 7)
    m2 = ModInt(5, 8)
    with pytest.raises(InvalidModOperationError):
        m1 < m2

def test_comparison_invalid_type():
    m1 = ModInt(2, 7)
    with pytest.raises(InvalidTypeOperationError):
        m1 < "string"

def test_totient():
    assert ModInt.totient(1) == 1
    assert ModInt.totient(2) == 1
    assert ModInt.totient(3) == 2
    assert ModInt.totient(4) == 2
    assert ModInt.totient(5) == 4
    assert ModInt.totient(9) == 6
    assert ModInt.totient(10) == 4
    assert ModInt.totient(21) == 12
    assert ModInt.totient(99) == 60
    assert ModInt.totient(100) == 40
    assert ModInt.totient(101) == 100 # Prime number

def test_totient_invalid():
    with pytest.raises(ValueError):
        ModInt.totient(0)
    with pytest.raises(ValueError):
        ModInt.totient(-5)
