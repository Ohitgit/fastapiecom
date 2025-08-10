from sqlalchemy import Column, Integer, String,ForeignKey,Text,Numeric,Date
from sqlalchemy.orm import relationship
from app.database import Base

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    suplier_id = Column(Integer, ForeignKey("supliers.id"), nullable=False)
    suplier = relationship("Suplier", backref="invoices")
    pharmacy_id = Column(Integer, ForeignKey("pharmacys.id"), nullable=False)
    pharmacy = relationship("Pharmacy", backref="invoices")
    credit_period = Column(Integer, nullable=True) 
    invoice_no = Column(String(128), nullable=False, index=True)  # invoice no str required
    remark = Column(Text, nullable=True)  
    pack_cost = Column(Numeric(10, 2), nullable=False)  # pack cost required
    pack_mrp = Column(Numeric(10, 2), nullable=False)   # pack mrp required
    grn_date = Column(Date, nullable=True)              # grn date date
    po_number = Column(Integer, nullable=False)         # po number int required
    dl_no = Column(Integer, nullable=True)              # dl no int
    invoice_date = Column(Date, nullable=True)          # invoice date date
    cancellation = Column(String(256), nullable=True)   

    def __repr__(self):
        return f"<InvoiceItem(id={self.id}, invoice_no={self.invoice_no})>"