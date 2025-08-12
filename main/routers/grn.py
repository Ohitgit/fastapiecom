from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from main.database import get_db
from main.schemas.grn import GRNCreate,GRNRead
from main.models.grn import GRN,GRNMedicine


router = APIRouter(prefix="/Grn", tags=["Grns"])

@router.post("/", response_model=GRNRead)
def create_grn(product: GRNCreate, db: Session = Depends(get_db)):
 
    product_data = product.dict()
    medicines_data = product_data.pop("medicines", [])

 
    new_grn = GRN(**product_data)


    new_grn.medicines = [GRNMedicine(**med) for med in medicines_data]

    # Save to DB
    db.add(new_grn)
    db.commit()
    db.refresh(new_grn)

    return new_grn



@router.get("/", response_model=list[GRNRead])
def get_grn(db: Session = Depends(get_db)):
    return db.query(GRN).all()


@router.get("/grn/{grn_id}", response_model=GRNRead)
def read_grn(grn_id: int, db: Session = Depends(get_db)):
    db_user = db.query(GRN).filter(GRN.id == grn_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Grn not found")
    return db_user


@router.put("/{grn_id}", response_model=GRNRead)
def update_grn(grn_id: int, product: GRNCreate, db: Session = Depends(get_db)):
    # 1. Find the GRN
    db_grn = db.query(GRN).filter(GRN.id == grn_id).first()
    if not db_grn:
        raise HTTPException(status_code=404, detail="GRN not found")

    # 2. Convert incoming data
    product_data = product.dict()
    medicines_data = product_data.pop("medicines", [])

    # 3. Update GRN basic fields
    for key, value in product_data.items():
        setattr(db_grn, key, value)

    # 4. Handle medicines
    db_grn.medicines.clear()  # remove existing medicines
    db_grn.medicines = [GRNMedicine(**med) for med in medicines_data]

    # 5. Save changes
    db.commit()
    db.refresh(db_grn)

    return db_grn
