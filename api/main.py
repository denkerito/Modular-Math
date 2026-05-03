from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from functools import reduce
import operator
from modMath import ModInt, ModIntException, CaesarCipher, AffineCipher, VigenereCipher, chinese_remainder_theorem
from .schemas import *

app = FastAPI(title="Modular Math API")

@app.exception_handler(ModIntException)
async def modint_exception_handler(request: Request, exc: ModIntException):
    """Cattura tutte le eccezioni custom della libreria e restituisce un errore HTTP 400."""
    return JSONResponse(
        status_code=400,
        content={"error": exc.__class__.__name__, "detail": str(exc)},
    )

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """Cattura gli errori di validazione (es. chiavi cifrario non valide) e restituisce 400."""
    return JSONResponse(
        status_code=400,
        content={"error": "ValidationError", "detail": str(exc)},
    )

@app.post("/op/add", response_model=ModMathResponse)
def add(data: Operation):
    result = ModInt(data.op1, data.mod) + data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/sub", response_model=ModMathResponse)
def sub(data: Operation):
    result = ModInt(data.op1, data.mod) - data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/mul", response_model=ModMathResponse)
def mul(data: Operation):
    result = ModInt(data.op1, data.mod) * data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/div", response_model=ModMathResponse)
def div(data: Operation):
    result = ModInt(data.op1, data.mod) / data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/pow", response_model=ModMathResponse)
def power(data: Operation):
    result = ModInt(data.op1, data.mod) ** data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/gcd", response_model=IntResponse)
def gcd(data: IntOperation):
    return IntResponse(result=ModInt.gcd(data.op1, data.op2))

@app.post("/op/egcd", response_model=EgcdResponse)
def egcd(data: IntOperation):
    values = ModInt.egcd(data.op1, data.op2)
    return EgcdResponse(gcd=values[0], x=values[1], y=values[2])

@app.post("/op/normalize", response_model=ModMathResponse)
def norm(data: UnaryOperation):
    result = ModInt(data.op1, data.mod)
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/inverse", response_model=ModMathResponse)
def inverse(data: UnaryOperation):
    result = ModInt(data.op1, data.mod).inverse()
    return ModMathResponse(result=result.value, mod=result.mod)

# --- Cryptography Endpoints ---

@app.post("/crypto/caesar/encrypt", response_model=CipherResponse)
def caesar_encrypt(data: CaesarRequest):
    cipher = CaesarCipher(data.key, data.alphabet)
    return CipherResponse(result=cipher.encrypt(data.text))

@app.post("/crypto/caesar/decrypt", response_model=CipherResponse)
def caesar_decrypt(data: CaesarRequest):
    cipher = CaesarCipher(data.key, data.alphabet)
    return CipherResponse(result=cipher.decrypt(data.text))

@app.post("/crypto/affine/encrypt", response_model=CipherResponse)
def affine_encrypt(data: AffineRequest):
    cipher = AffineCipher(data.a, data.b, data.alphabet)
    return CipherResponse(result=cipher.encrypt(data.text))

@app.post("/crypto/affine/decrypt", response_model=CipherResponse)
def affine_decrypt(data: AffineRequest):
    cipher = AffineCipher(data.a, data.b, data.alphabet)
    return CipherResponse(result=cipher.decrypt(data.text))

@app.post("/crypto/vigenere/encrypt", response_model=CipherResponse)
def vigenere_encrypt(data: VigenereRequest):
    cipher = VigenereCipher(data.keyword, data.alphabet)
    return CipherResponse(result=cipher.encrypt(data.text))

@app.post("/crypto/vigenere/decrypt", response_model=CipherResponse)
def vigenere_decrypt(data: VigenereRequest):
    cipher = VigenereCipher(data.keyword, data.alphabet)
    return CipherResponse(result=cipher.decrypt(data.text))

# --- Number Theory Endpoints ---

@app.post("/op/crt", response_model=CRTResponse)
def crt(data: CRTRequest):
    result = chinese_remainder_theorem(data.remainders, data.moduli)
    modulus = reduce(operator.mul, data.moduli, 1)
    return CRTResponse(result=result, modulus=modulus)