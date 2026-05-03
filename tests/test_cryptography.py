import pytest
from modMath import CaesarCipher, AffineCipher

def test_caesar_encrypt():
    cipher = CaesarCipher(3)
    assert cipher.encrypt("ABC") == "DEF"
    assert cipher.encrypt("XYZ") == "ABC"
    assert cipher.encrypt("HELLO WORLD") == "KHOOR ZRUOG"

def test_caesar_decrypt():
    cipher = CaesarCipher(3)
    assert cipher.decrypt("DEF") == "ABC"
    assert cipher.decrypt("ABC") == "XYZ"
    assert cipher.decrypt("KHOOR ZRUOG") == "HELLO WORLD"

def test_caesar_custom_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = CaesarCipher(5, alphabet)
    assert cipher.encrypt("abc") == "fgh"
    assert cipher.decrypt("fgh") == "abc"

def test_caesar_negative_key():
    cipher = CaesarCipher(-3)
    assert cipher.encrypt("DEF") == "ABC"
    assert cipher.decrypt("ABC") == "DEF"

def test_caesar_empty_alphabet():
    with pytest.raises(ValueError):
        CaesarCipher(3, "")

def test_affine_cipher_encrypt():
    # Formula: E(x) = (5x + 8) mod 26
    # A=0 -> (0+8)%26 = 8 (I)
    # B=1 -> (5+8)%26 = 13 (N)
    # C=2 -> (10+8)%26 = 18 (S)
    cipher = AffineCipher(5, 8)
    assert cipher.encrypt("ABC") == "INS"
    assert cipher.encrypt("HELLO WORLD") == "RCLLA OAPLX"

def test_affine_cipher_decrypt():
    cipher = AffineCipher(5, 8)
    assert cipher.decrypt("INS") == "ABC"
    assert cipher.decrypt("RCLLA OAPLX") == "HELLO WORLD"

def test_affine_cipher_invalid_key_a():
    # 2 is not coprime to 26
    with pytest.raises(ValueError, match="must be coprime"):
        AffineCipher(2, 3)

def test_affine_cipher_custom_alphabet():
    alphabet = "0123456789"
    # mod 10, a=3 (coprime)
    cipher = AffineCipher(3, 1, alphabet)
    assert cipher.encrypt("123") == "470" # (3*1+1)%10=4, (3*2+1)%10=7, (3*3+1)%10=0
    assert cipher.decrypt("470") == "123"

def test_affine_cipher_non_alphabet_characters():
    cipher = AffineCipher(5, 8)
    # Lowercase letters and numbers should remain unchanged with default uppercase alphabet
    assert cipher.encrypt("abc 123!") == "abc 123!"
