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
