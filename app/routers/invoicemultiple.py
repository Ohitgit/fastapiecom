from fastapi import APIRouter, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas


router = APIRouter(prefix="/multipleinvoice", tags=["MultipleInvoice"])

@router.post("/", response_model=schemas.InvoiceMultipleRead)
def create_invoice_multiple(data: schemas.InvoiceMultipleCreate, db: Session = Depends(get_db)):
    obj = models.InvoiceMultiple()
    
    if data.invoice_ids:
        invoices = db.query(models.Invoice).filter(
            models.Invoice.id.in_(data.invoice_ids)
        ).all()
        obj.invoices = invoices
    
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[schemas.InvoiceMultipleBase])
def get_invoice_multiple(db: Session = Depends(get_db)):
    return db.query(models.InvoiceMultiple).all()