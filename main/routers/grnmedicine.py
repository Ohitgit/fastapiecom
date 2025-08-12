from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main.database import get_db
from main.schemas.grnmedicine import GRNMedicineCreate,GRNMedicinceRead
from main.models.grn import GRN,GRNMedicine


router = APIRouter(prefix="/Grnmedicine", tags=["Grnmedicine"])

@router.post("/", response_model=GRNMedicinceRead)
def create_grnmedicine(product: GRNMedicineCreate, db: Session = Depends(get_db)):
 
    product_data =GRNMedicineCreate(**product.dict())
    # Save to DB
    db.add(product_data)
    db.commit()
    db.refresh(product_data)

    return product_data



@router.get("/", response_model=list[GRNMedicinceRead])
def get_grnmedicine(db: Session = Depends(get_db)):
    return db.query(GRNMedicine).all()
