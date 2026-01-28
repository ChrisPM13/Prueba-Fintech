from pydantic import BaseModel


class ApplicationCreate(BaseModel):
    name: str
    rfc: str
    curp: str
    gender: str
    income: float
    address_input: str

class ApplicationResponse(BaseModel):
    id: int
    name: str
    rfc: str
    curp: str
    gender: str
    income: float
    address_input: str
    status: str
    credit_score: int
    explanation: str

    class Config:
        orm_mode = True
