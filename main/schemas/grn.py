from pydantic import BaseModel
from typing import List, Optional
from datetime import date

from decimal import Decimal
from main.schemas.grnmedicine import GRNMedicineCreate

class GRNBase(BaseModel):
    grn_status: str
    po_number: Optional[str] = None
    po_date: Optional[date] = None
    dl_no: Optional[str] = None
    gstin_no: Optional[str] = None
    invoice_number: str
    invoice_date: date
    recieved_by: Optional[str] = None
    remarks: Optional[str] = None
    cancellation_remarks: Optional[str] = None
    total_amount: Optional[Decimal] = 0
    cgst_amount: Optional[Decimal] = 0
    sgst_amount: Optional[Decimal] = 0
    igst_amount: Optional[Decimal] = 0
    import_duty: Optional[Decimal] = 0
    cash_discount: Optional[Decimal] = 0
    la_amount: Optional[Decimal] = 0
    insurance_amount: Optional[Decimal] = 0
    other_amount: Optional[Decimal] = 0
    round_off_amount: Optional[Decimal] = 0
    net_amount: Optional[Decimal] = 0

    counter: str
    supplier: str
    unit: str
    medicines: List[GRNMedicineCreate]


class GRNCreate(GRNBase):
    grn_status: str
    po_number: Optional[str] = None
    po_date: Optional[date] = None
    dl_no: Optional[str] = None
    gstin_no: Optional[str] = None
    invoice_number: str
    invoice_date: date
    recieved_by: Optional[str] = None
    remarks: Optional[str] = None
    cancellation_remarks: Optional[str] = None
    total_amount: Optional[Decimal] = 0
    cgst_amount: Optional[Decimal] = 0
    sgst_amount: Optional[Decimal] = 0
    igst_amount: Optional[Decimal] = 0
    import_duty: Optional[Decimal] = 0
    cash_discount: Optional[Decimal] = 0
    la_amount: Optional[Decimal] = 0
    insurance_amount: Optional[Decimal] = 0
    other_amount: Optional[Decimal] = 0
    round_off_amount: Optional[Decimal] = 0
    net_amount: Optional[Decimal] = 0

    counter: str
    supplier: str
    unit: str
    medicines: List[GRNMedicineCreate]


class GRNRead(GRNBase):
    id: int
    
    class Config:
        orm_mode = True


class MultipleGRNCreate(BaseModel):
    grns: List[GRNCreate]

