from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.post("/", response_model=schemas.InvoiceRead)
def create_product(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):

    # Check if invoice already exists
    existing_invoice = db.query(models.Invoice).filter(
        models.Invoice.suplier_id == invoice.suplier_id,
        models.Invoice.pharmacy_id == invoice.pharmacy_id
    ).first()

    if existing_invoice:
        raise HTTPException(status_code=400, detail="Invoice for this supplier and pharmacy already exists")
    
    invoice_data1 = invoice.dict()
    for new1 in invoice_data1['multiples']:
      multiple_obj = models.InvoiceMultiple(**new1)
      db.add(multiple_obj)
    # Exclude multiples from invoice dict
    invoice_data = invoice.dict(exclude={"multiples"})

    # Create main invoice
    new_invoice = models.Invoice(**invoice_data)
    db.add(new_invoice)

   


    db.commit()
    db.refresh(new_invoice)

    return new_invoice


@router.get("/", response_model=list[schemas.InvoiceRead])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Invoice).all()
