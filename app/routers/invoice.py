from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.post("/", response_model=schemas.InvoiceRead)
def create_product(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    existing_invoice = db.query(models.Invoice).filter( models.Invoice.suplier_id == invoice.suplier_id, models.Invoice.pharmacy_id == invoice.pharmacy_id).first()
    if existing_invoice:
      raise HTTPException(status_code=400, detail="Invoice for this supplier and pharmacy already exists")

    new_product = models.Invoice(**invoice.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=list[schemas.InvoiceRead])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Invoice).all()
