from pydantic import BaseModel, Field

class Operation(BaseModel):
    op1 : int
    op2 : int
    mod : int = Field(gt = 1)

class UnaryOperation(BaseModel):
    op1 : int
    mod : int = Field(gt = 1)

class IntOperation(BaseModel):
    op1: int
    op2: int

class ModMathResponse(BaseModel):
    result: int
    mod: int = Field(gt = 1)

class IntResponse(BaseModel):
    result: int

class EgcdResponse(BaseModel):
    gcd: int
    x: int
    y: int

class CipherResponse(BaseModel):
    result: str

class CaesarRequest(BaseModel):
    text: str
    key: int
    alphabet: str | None = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class AffineRequest(BaseModel):
    text: str
    a: int
    b: int
    alphabet: str | None = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class VigenereRequest(BaseModel):
    text: str
    keyword: str
    alphabet: str | None = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class CRTRequest(BaseModel):
    remainders: list[int]
    moduli: list[int]

class CRTResponse(BaseModel):
    result: int
    modulus: int