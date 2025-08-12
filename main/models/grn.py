
from sqlalchemy import Column, Integer, String,ForeignKey,Text,Numeric,Date,Table
from sqlalchemy.orm import relationship
from main.database import Base
from .grnmedicine import GRNMedicine

class GRN(Base):
    __tablename__ = "pharmacy_grn"
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    grn_status = Column(String(100), nullable=False)
    po_number = Column(String(50), nullable=True)
    po_date = Column(Date, nullable=True)
    dl_no = Column(String(50), nullable=True)
    gstin_no = Column(String(50), nullable=True)
    invoice_number = Column(String(50), nullable=False)
    invoice_date = Column(Date, nullable=False)
    recieved_by = Column(String(50), nullable=True)
    remarks = Column(String(50), nullable=True)
    cancellation_remarks = Column(String(50), nullable=True)
    total_amount = Column(Numeric(9, 2), default=0)
    cgst_amount = Column(Numeric(9, 2), default=0)
    sgst_amount = Column(Numeric(9, 2), default=0)
    igst_amount = Column(Numeric(9, 2), default=0)
    import_duty = Column(Numeric(9, 2), default=0)
    cash_discount = Column(Numeric(9, 2), default=0)
    la_amount = Column(Numeric(9, 2), default=0)
    insurance_amount = Column(Numeric(9, 2), default=0)
    other_amount = Column(Numeric(9, 2), default=0)
    round_off_amount = Column(Numeric(9, 2), default=0)
    net_amount = Column(Numeric(9, 2), default=0)

    counter = Column(String(50), nullable=True)
    supplier= Column(String(50), nullable=True)
    unit = Column(String(50), nullable=True)
    medicines = relationship("GRNMedicine", back_populates="grn", cascade="all, delete-orphan")

  

