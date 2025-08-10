from pydantic import BaseModel


class PharmacyBase(BaseModel):
    name: str


class PharmacyCreate(PharmacyBase):
    pass

class PharmacyRead(PharmacyBase):
    id: int

    class Config:
        orm_mode = True
