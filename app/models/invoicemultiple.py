


from sqlalchemy import Column, Integer, String, Table, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base
from .invoice import invoice_invoice_multiple

class InvoiceMultiple(Base):
    __tablename__ = "invoices_multiple"

    id = Column(Integer, primary_key=True, index=True)


    invoices = relationship(
        "Invoice",
        secondary=invoice_invoice_multiple,
        back_populates="multiples"
    )

   
