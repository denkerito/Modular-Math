from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from modMath import ModInt, ModIntException
from .schemas import *

app = FastAPI(title="Modular Math API")

@app.exception_handler(ModIntException)
async def modint_exception_handler(request: Request, exc: ModIntException):
    """Cattura tutte le eccezioni custom della libreria e restituisce un errore HTTP 400."""
    return JSONResponse(
        status_code=400,
        content={"error": exc.__class__.__name__, "detail": str(exc)},
    )

@app.post("/op/add", response_model=ModMathResponse)
async def add(data: Operation):
    result = ModInt(data.op1, data.mod) + data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/sub", response_model=ModMathResponse)
async def sub(data: Operation):
    result = ModInt(data.op1, data.mod) - data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/mul", response_model=ModMathResponse)
async def mul(data: Operation):
    result = ModInt(data.op1, data.mod) * data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/div", response_model=ModMathResponse)
async def div(data: Operation):
    result = ModInt(data.op1, data.mod) / data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/pow", response_model=ModMathResponse)
async def power(data: Operation):
    result = ModInt(data.op1, data.mod) ** data.op2
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/gcd", response_model=IntResponse)
async def gcd(data: IntOperation):
    return IntResponse(result=ModInt.gcd(data.op1, data.op2))

@app.post("/op/egcd", response_model=EgcdResponse)
async def egcd(data: IntOperation):
    values = ModInt.egcd(data.op1, data.op2)
    return EgcdResponse(gcd=values[0], x=values[1], y=values[2])

@app.post("/op/normalize", response_model=ModMathResponse)
async def norm(data: UnaryOperation):
    result = ModInt(data.op1, data.mod)
    return ModMathResponse(result=result.value, mod=result.mod)

@app.post("/op/inverse", response_model=ModMathResponse)
async def inverse(data: UnaryOperation):
    result = ModInt(data.op1, data.mod).inverse()
    return ModMathResponse(result=result.value, mod=result.mod)