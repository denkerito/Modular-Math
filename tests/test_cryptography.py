import pytest
from modMath import CaesarCipher, AffineCipher, VigenereCipher

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

def test_vigenere_cipher_encrypt():
    # Key: KEY (K=10, E=4, Y=24)
    # H(7) + K(10) = 17 (R)
    # E(4) + E(4)  = 8 (I)
    # L(11) + Y(24) = 35 % 26 = 9 (J)
    # L(11) + K(10) = 21 (V)
    # O(14) + E(4)  = 18 (S)
    cipher = VigenereCipher("KEY")
    assert cipher.encrypt("HELLO") == "RIJVS"

def test_vigenere_cipher_decrypt():
    cipher = VigenereCipher("KEY")
    assert cipher.decrypt("RIJVS") == "HELLO"

def test_vigenere_cipher_keyword_advancement():
    # Key: AB (A=0, B=1)
    # H(7) + A(0) = 7 (H)
    # E(4) + B(1) = 5 (F)
    # Space (skip)
    # L(11) + A(0) = 11 (L)
    # L(11) + B(1) = 12 (M)
    # O(14) + A(0) = 14 (O)
    cipher = VigenereCipher("AB")
    assert cipher.encrypt("HE LLO") == "HF LMO"
    assert cipher.decrypt("HF LMO") == "HE LLO"

def test_vigenere_cipher_invalid_keyword():
    with pytest.raises(ValueError, match="Keyword cannot be empty"):
        VigenereCipher("", "ABC")
    with pytest.raises(ValueError, match="character '1' not in alphabet"):
        VigenereCipher("KEY1", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def test_vigenere_cipher_custom_alphabet():
    alphabet = "0123456789"
    # Key: 12 (1, 2)
    # 5 + 1 = 6
    # 6 + 2 = 8
    cipher = VigenereCipher("12", alphabet)
    assert cipher.encrypt("56") == "68"
    assert cipher.decrypt("68") == "56"
