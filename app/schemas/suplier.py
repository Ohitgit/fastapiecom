from pydantic import BaseModel


class SuplierBase(BaseModel):
    name: str


class SuplierCreate(SuplierBase):
    pass

class SuplierRead(SuplierBase):
    id: int

    class Config:
        orm_mode = True
