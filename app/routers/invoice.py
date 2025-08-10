from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.post("/", response_model=schemas.InvoiceRead)
def create_product(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    suplier = db.query(models.Suplier).filter(models.Suplier.id == invoice.suplier_id).first()
    if suplier:
        raise HTTPException(status_code=400, detail="Suplier already exists")
    
    pharmacy = db.query(models.Pharmacy).filter(models.Pharmacy.id == invoice.pharmacy_id).first()
    if pharmacy:
        raise HTTPException(status_code=400, detail="Pharmacy already exists")
    new_product = models.Invoice(**invoice.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=list[schemas.InvoiceRead])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Invoice).all()
