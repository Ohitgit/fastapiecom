from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/suplier", tags=["Supliers"])

@router.post("/", response_model=schemas.SuplierRead)
def create_category(category: schemas.SuplierCreate, db: Session = Depends(get_db)):
    # db_category = db.query(models.Suplier).filter(models.Suplier.name == category.name).first()
    # if db_category:
    #     raise HTTPException(status_code=400, detail="Category already exists")
    new_category = models.Suplier(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.get("/", response_model=list[schemas.SuplierRead])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Suplier).all()
