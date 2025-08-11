from pydantic import BaseModel, conint, constr,Field
from typing import Optional
from datetime import date
from decimal import Decimal
from .suplier import SuplierRead
from .pharmacy import PharmacyRead
from enum import Enum

class UnitType(str, Enum):
    TABLET= "Tablet"
    GEL = "Gel"
    

class InvoiceBase(BaseModel):
    suplier_id: int
    pharmacy_id:int
    credit_period: Optional[conint(ge=0)] = None
    invoice_no: str
    remark: str
    medicine_name: str
    unit: UnitType
    pack_cost: Decimal = Field(..., description="Pack cost (decimal)")
    pack_mrp: Decimal = Field(..., description="Pack MRP (decimal)")

    grn_date: Optional[date] = None
    po_number: int = Field(..., description="PO number")
    dl_no: Optional[int] = None
    invoice_date: Optional[date] = None
    cancellation: Optional[str] = None
    ex_date: Optional[date] = None
    batch_no: constr(strip_whitespace=True, max_length=128) = Field(..., description="Batch number")

    rec_qty: conint(ge=0) = Field(..., description="Received quantity")
    free_qty: Optional[conint(ge=0)] = Field(0, description="Free quantity")
    sheet_qty: conint(ge=0) = Field(..., description="Sheet quantity")
    qoh: conint(ge=0) = Field(..., description="Quantity on hand")

    # optional integer forms (if you need them as int)
    pack_cost_int: Optional[int] = None
    pack_mrp_int: Optional[int] = None

    disc: Optional[conint(ge=0)] = None
    total_amt: Optional[Decimal] = None

    cgst: Decimal = Field(..., description="CGST amount or percent")
    sgst: Decimal = Field(..., description="SGST amount or percent")
    igst: Optional[Decimal] = None

    total_mrp: Optional[Decimal] = None


class InvoiceCreate(InvoiceBase):
    pass

class InvoiceRead(InvoiceBase):
    id: int
    suplier: SuplierRead
    pharmacy:PharmacyRead

    class Config:
        orm_mode = True
