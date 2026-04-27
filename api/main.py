from fastapi import FastAPI
from modMath import ModInt
from .schemas import Operation, UnaryOperation, IntOperation

app = FastAPI(title="Modular Math API")

@app.post("/op/add")
def add(data: Operation):
    return ModInt(data.op1, data.mod) + data.op2

@app.post("/op/sub")
def sub(data: Operation):
    return ModInt(data.op1, data.mod) - data.op2

@app.post("/op/mul")
def sub(data: Operation):
    return ModInt(data.op1, data.mod) * data.op2

@app.post("/op/div")
def div(data: Operation):
    return ModInt(data.op1, data.mod) / data.op2

@app.post("/op/pow")
def sub(data: Operation):
    return ModInt(data.op1, data.mod) ** data.op2

@app.post("/op/gcd")
def gcd(data: IntOperation):
    return {"gcd": ModInt.gcd(data.op1, data.op2)}

@app.post("/op/egcd")
def egcd(data: IntOperation):
    values = ModInt.egcd(data.op1, data.op2)
    return {"gcd": values[0], "x": values[1], "y": values[2]}

@app.post("/op/normalize")
def norm(data: UnaryOperation):
    return ModInt(data.op1, data.mod)

@app.post("/op/inverse")
def inverse(data: UnaryOperation):
    return ModInt(data.op1, data.mod).inverse()