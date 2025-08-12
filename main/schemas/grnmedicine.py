
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

from decimal import Decimal

class GRNMedicineBase(BaseModel):
    medicine_name: str
    exp_date: date
    batch_no: str
    received_qty: int
    free_qty: Optional[int] = 0
    sheet_qty: int
    qoh: int
    unit: str
    pack_cost: Decimal
    pack_mrp: Decimal
    discount_percent: Optional[Decimal] = 0
    total_amount: Decimal
    cgst_percent: Optional[Decimal] = 0
    sgst_percent: Optional[Decimal] = 0
    igst_percent: Optional[Decimal] = 0
    tab_mrp: Optional[Decimal] = 0


class GRNMedicineCreate(GRNMedicineBase):
     pass


class GRNMedicinceRead(GRNMedicineBase):
    id: int

    class Config:
        orm_mode = True