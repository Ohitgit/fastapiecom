from pydantic import BaseModel, conint, constr
from typing import Optional
from datetime import date
from decimal import Decimal
from .suplier import SuplierRead
from .pharmacy import PharmacyRead


class InvoiceBase(BaseModel):
    suplier_id: int
    pharmacy_id:int
    credit_period: Optional[conint(ge=0)] = None
    invoice_no: constr(strip_whitespace=True, max_length=128)
    remark: Optional[str] = None
    pack_cost: Decimal
    pack_mrp: Decimal
    grn_date: Optional[date] = None
    po_number: int
    dl_no: Optional[int] = None
    invoice_date: Optional[date] = None
    cancellation: Optional[str] = None


class InvoiceCreate(InvoiceBase):
    pass

class InvoiceRead(InvoiceBase):
    id: int
    suplier: SuplierRead
    pharmacy:PharmacyRead

    class Config:
        orm_mode = True
