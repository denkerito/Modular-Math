from pydantic import BaseModel, Field

class Operation(BaseModel):
    op1 : int
    op2 : int
    mod : int = Field(gt = 1)