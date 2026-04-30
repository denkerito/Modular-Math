import pytest
from modMath import CaesarCipher

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
