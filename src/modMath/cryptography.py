from modMath import ModInt

class CaesarCipher:
    """
    Implementation of the Caesar cipher using the ModInt class.
    
    The Caesar cipher is a substitution cipher where each letter in the plaintext 
    is replaced by a letter some fixed number of positions down the alphabet.
    """
    def __init__(self, key: int, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if not alphabet:
            raise ValueError("Alphabet cannot be empty")
        self.key = key
        self.alphabet = alphabet
        self.mod = len(alphabet)
        self.char_to_idx = {char: i for i, char in enumerate(alphabet)}
        self.idx_to_char = {i: char for i, char in enumerate(alphabet)}

    def encrypt(self, text: str) -> str:
        """Encrypts the text using the shift key."""
        result = []
        for char in text:
            if char in self.char_to_idx:
                idx = self.char_to_idx[char]
                # Using ModInt for modular addition
                encrypted_idx = (ModInt(idx, self.mod) + self.key).value
                result.append(self.idx_to_char[encrypted_idx])
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, text: str) -> str:
        """Decrypts the text using the shift key."""
        result = []
        for char in text:
            if char in self.char_to_idx:
                idx = self.char_to_idx[char]
                # Using ModInt for modular subtraction
                decrypted_idx = (ModInt(idx, self.mod) - self.key).value
                result.append(self.idx_to_char[decrypted_idx])
            else:
                result.append(char)
        return "".join(result)


class AffineCipher:
    """
    Implementation of the Affine cipher using the ModInt class.
    
    The Affine cipher is a substitution cipher where each letter in the plaintext 
    is replaced by a letter according to the formula: E(x) = (ax + b) mod m, 
    where 'a' and 'm' must be coprime.
    """
    def __init__(self, a: int, b: int, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if not alphabet:
            raise ValueError("Alphabet cannot be empty")
        
        mod = len(alphabet)
        if ModInt.gcd(a, mod) != 1:
            raise ValueError(f"Key 'a' ({a}) must be coprime to the alphabet length ({mod}).")
            
        self.a = a
        self.b = b
        self.alphabet = alphabet
        self.mod = mod
        self.char_to_idx = {char: i for i, char in enumerate(alphabet)}
        self.idx_to_char = {i: char for i, char in enumerate(alphabet)}

    def encrypt(self, text: str) -> str:
        """Encrypts the text using the affine keys (a, b)."""
        result = []
        for char in text:
            if char in self.char_to_idx:
                idx = self.char_to_idx[char]
                # Formula: E(x) = (ax + b) mod m
                encrypted_idx = (ModInt(idx, self.mod) * self.a + self.b).value
                result.append(self.idx_to_char[encrypted_idx])
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, text: str) -> str:
        """Decrypts the text using the affine keys (a, b)."""
        result = []
        for char in text:
            if char in self.char_to_idx:
                idx = self.char_to_idx[char]
                # Formula: D(x) = a^-1 * (x - b) mod m
                # ModInt division automatically handles the modular inverse
                decrypted_idx = ((ModInt(idx, self.mod) - self.b) / self.a).value
                result.append(self.idx_to_char[decrypted_idx])
            else:
                result.append(char)
        return "".join(result)


class VigenereCipher:
    """
    Implementation of the Vigenère cipher using the ModInt class.
    
    The Vigenère cipher is a polyalphabetic substitution cipher that uses a 
    keyword to determine the shift for each letter in the plaintext.
    """
    def __init__(self, keyword: str, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if not alphabet:
            raise ValueError("Alphabet cannot be empty")
        if not keyword:
            raise ValueError("Keyword cannot be empty")
            
        self.alphabet = alphabet
        self.mod = len(alphabet)
        self.char_to_idx = {char: i for i, char in enumerate(alphabet)}
        self.idx_to_char = {i: char for i, char in enumerate(alphabet)}
        
        # Pre-calculate keyword indices for efficiency
        self.keyword_indices = []
        for char in keyword:
            if char not in self.char_to_idx:
                raise ValueError(f"Keyword character '{char}' not in alphabet")
            self.keyword_indices.append(self.char_to_idx[char])
        self.keyword = keyword

    def encrypt(self, text: str) -> str:
        """Encrypts the text using the keyword."""
        result = []
        key_idx = 0
        key_len = len(self.keyword_indices)
        
        for char in text:
            if char in self.char_to_idx:
                shift = self.keyword_indices[key_idx % key_len]
                idx = self.char_to_idx[char]
                # Formula: E(i) = (P(i) + K(i)) mod m
                encrypted_idx = (ModInt(idx, self.mod) + shift).value
                result.append(self.idx_to_char[encrypted_idx])
                key_idx += 1
            else:
                result.append(char)
        return "".join(result)

    def decrypt(self, text: str) -> str:
        """Decrypts the text using the keyword."""
        result = []
        key_idx = 0
        key_len = len(self.keyword_indices)
        
        for char in text:
            if char in self.char_to_idx:
                shift = self.keyword_indices[key_idx % key_len]
                idx = self.char_to_idx[char]
                # Formula: D(i) = (C(i) - K(i)) mod m
                decrypted_idx = (ModInt(idx, self.mod) - shift).value
                result.append(self.idx_to_char[decrypted_idx])
                key_idx += 1
            else:
                result.append(char)
        return "".join(result)
