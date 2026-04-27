from fastapi import FastAPI
from modMath import ModInt
from schemas import Operation

app = FastAPI(title="Modular Math API")

@app.post("/add")
def add(data: Operation):
    return {"result" : ModInt(data.op1, data.mod) + data.op2, "mod": data.mod}


