from sqlalchemy import Column, Integer, String,ForeignKey,Text,Numeric,Date,Table
from sqlalchemy.orm import relationship
from app.database import Base
invoice_invoice_multiple = Table(
    "invoice_invoice_multiple",
    Base.metadata,
    Column("invoice_id", Integer, ForeignKey("invoices.id", ondelete="CASCADE"), primary_key=True),
    Column("invoice_multiple_id", Integer, ForeignKey("invoices_multiple.id", ondelete="CASCADE"), primary_key=True)
)

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    suplier_id = Column(Integer, ForeignKey("supliers.id"), nullable=False)
    suplier = relationship("Suplier", backref="invoices")
    pharmacy_id = Column(Integer, ForeignKey("pharmacys.id"), nullable=False)
    pharmacy = relationship("Pharmacy", backref="invoices")
    credit_period = Column(Integer, nullable=True)       # credit period int

    invoice_no = Column(String(128), nullable=False, index=True)  # invoice no str required
    remark = Column(Text, nullable=True)                # remark str

    medicine_name = Column(String(256), nullable=False) # medicine name str required
    unit = Column(String(64), nullable=False)           # unit dropdown required

    # Use numeric for costs/prices; precision scale set to 10,2 (change as needed)
    pack_cost = Column(Numeric(10, 2), nullable=False)  # pack cost required
    pack_mrp = Column(Numeric(10, 2), nullable=False)   # pack mrp required

    grn_date = Column(Date, nullable=True)              # grn date date
    po_number = Column(Integer, nullable=False)         # po number int required
    dl_no = Column(Integer, nullable=True)              # dl no int
    invoice_date = Column(Date, nullable=True)          # invoice date date
    cancellation = Column(String(256), nullable=True)   # cancellation str
    ex_date = Column(Date, nullable=True)               # ex date date
    batch_no = Column(String(128), nullable=False)      # batch no str required

    rec_qty = Column(Integer, nullable=False)           # rec qty int required
    free_qty = Column(Integer, nullable=True, default=0) # free qty int
    sheet_qty = Column(Integer, nullable=False)         # sheet qty int required
    qoh = Column(Integer, nullable=False)               # qoh int required

    pack_cost_int = Column(Integer, nullable=True)      # optional: if you need integer pack cost
    pack_mrp_int = Column(Integer, nullable=True)       # optional: if you need integer pack mrp

    disc = Column(Integer, nullable=True)               # disc int (percentage or absolute - clarify)
    total_amt = Column(Numeric(12, 2), nullable=True)   # total amt int/decimal

    cgst = Column(Numeric(6, 2), nullable=False)        # cgst required
    sgst = Column(Numeric(6, 2), nullable=False)        # sgst required
    igst = Column(Numeric(6, 2), nullable=True)         # igst int

    total_mrp = Column(Numeric(12, 2), nullable=True)   # total mrp int/decimal

    multiples = relationship(
        "InvoiceMultiple",
        secondary=invoice_invoice_multiple,
        back_populates="invoices"
    )

    def __repr__(self):
        return f"<InvoiceItem(id={self.id}, invoice_no={self.invoice_no}, medicine={self.medicine_name})>"