
from sqlalchemy import Column, Integer, String,ForeignKey,Text,Numeric,Date,Table
from sqlalchemy.orm import relationship
from main.database import Base


class GRNMedicine(Base):

    __tablename__ = "pharmacy_grn_medicines"
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    medicine_name = Column(String, nullable=False)
    exp_date = Column(Date, nullable=False)
    batch_no = Column(String, nullable=False)
    received_qty = Column(Integer, nullable=False)
    free_qty = Column(Integer, default=0)
    sheet_qty = Column(Integer, nullable=False)
    qoh = Column(Integer, nullable=False)

    unit = Column(String, nullable=False)
    pack_cost = Column(Numeric(9, 2), nullable=False)
    pack_mrp = Column(Numeric(9, 2), nullable=False)
    discount_percent = Column(Numeric(5, 2), default=0)
    total_amount = Column(Numeric(9, 2), nullable=False)
    cgst_percent = Column(Numeric(5, 2), default=0)
    sgst_percent = Column(Numeric(5, 2), default=0)
    igst_percent = Column(Numeric(5, 2), default=0)
    tab_mrp = Column(Numeric(9, 2), default=0)

    grn_id = Column( Integer, ForeignKey("pharmacy_grn.id", ondelete="CASCADE"), nullable=False)
    grn = relationship("GRN", back_populates="medicines")

