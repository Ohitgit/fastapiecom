from typing import List, Optional
from pydantic import BaseModel
from .invoice import InvoiceRead

class InvoiceMultipleBase(BaseModel):
       pass
  

class InvoiceMultipleCreate(InvoiceMultipleBase):
    invoice_ids: List[int] = []  # link products while creating

class InvoiceMultipleRead(InvoiceMultipleBase):
    id: int
    invoices: List[InvoiceRead] = []

    class Config:
        orm_mode = True