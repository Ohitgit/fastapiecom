from fastapi import APIRouter, Depends,Query, HTTPException
from sqlalchemy.orm import Session
from main.database import get_db
from main.schemas.grn import GRNCreate,GRNRead
from main.models.grn import GRN,GRNMedicine
from datetime import date
from typing import Optional


router = APIRouter(prefix="/Grn", tags=["Grns"])

@router.post("/", response_model=GRNRead)
def create_grn(product: GRNCreate, db: Session = Depends(get_db)):
    product_data = product.dict()
    medicines_data = product_data.pop("medicines", [])
    new_grn = GRN(**product_data)
    new_grn.medicines = [GRNMedicine(**med) for med in medicines_data]
    db.add(new_grn)
    db.commit()
    db.refresh(new_grn)
    return new_grn



@router.get("/", response_model=list[GRNRead])
def get_grn(db: Session = Depends(get_db)):
    ''' grn all data retrive '''
    return db.query(GRN).all()


@router.get("/grn/{grn_id}", response_model=GRNRead)
def read_grn(grn_id: int, db: Session = Depends(get_db)):
    ''' particular grn data reterive '''
    db_user = db.query(GRN).filter(GRN.id == grn_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Grn not found")
    return db_user


@router.put("/{grn_id}", response_model=GRNRead)
def update_grn(grn_id: int, product: GRNCreate, db: Session = Depends(get_db)):
    db_grn = db.query(GRN).filter(GRN.id == grn_id).first()
    if not db_grn:
        raise HTTPException(status_code=404, detail="GRN not found")
    product_data = product.dict()
    medicines_data = product_data.pop("medicines", [])
    for key, value in product_data.items():
        setattr(db_grn, key, value)
    db_grn.medicines.clear()  
    db_grn.medicines = [GRNMedicine(**med) for med in medicines_data]

    db.commit()
    db.refresh(db_grn)
    return db_grn

@router.get("/grn_filter", response_model=list[GRNRead])
def filter_grn( grn_code: str = Query(..., example="GRN_1", description="Enter GRN ID with prefix"),from_date: Optional[date] = Query(None),to_date: Optional[date] = Query(None),db: Session = Depends(get_db)):
    """
    Filter GRN records between given dates, by GRN code.
    Args: strat to filter From Date to To Date and using by Grn_id
    """
    # Extract numeric part from GRN_1 → 1
    if grn_code.startswith("GRN_"):
        grn_id = int(grn_code.replace("GRN_", ""))
    else:
        raise ValueError("GRN code must start with 'GRN_'")

    query = db.query(GRN).filter(GRN.id == grn_id)

    if from_date and to_date:
        query = query.filter(GRN.invoice_date.between(from_date, to_date))

    return query.all()
