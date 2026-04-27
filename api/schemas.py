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