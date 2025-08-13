from fastapi import APIRouter, Depends,Query, HTTPException
from sqlalchemy.orm import Session
from main.database import get_db
from main.schemas.grn import GRNCreate,GRNRead
from main.models.grn import GRN,GRNMedicine
from datetime import date,datetime
from typing import Optional
from sqlalchemy import func

router = APIRouter(prefix="/Grn", tags=["Grns"])


@router.post("/create_grn", response_model=GRNRead)
def create_grn(product: GRNCreate, db: Session = Depends(get_db)):
    """
    Create a new GRN (Goods Receipt Note) record along with its associated medicines.

    This endpoint allows the creation of a GRN entry in the database.
    The GRN details are provided through the `product` payload, which may
    also include a list of medicines. Each medicine is linked to the created GRN.

    Args:
        product (GRNCreate): Pydantic model containing GRN details and an optional
            list of medicines to be linked with this GRN.
        db (Session): SQLAlchemy database session dependency.

    Returns:
        GRNRead: The newly created GRN record with its associated medicines.
    """
    product_data = product.dict()
    medicines_data = product_data.pop("medicines", []) # this key only skip 
    new_grn = GRN(**product_data) # then insert data
    new_grn.medicines = [GRNMedicine(**med) for med in medicines_data] # medicines  key skip here then insert data all the medicines data inserted here
    db.add(new_grn)
    db.commit()
    db.refresh(new_grn)
    return new_grn

@router.get("/read_grn", response_model=list[GRNRead])
def read_grn(grn_id: int, db: Session = Depends(get_db)):
    """
    Retrieve GRN records by GRN ID.

    This endpoint fetches all Goods Receipt Note (GRN) records
    from the database that match the provided `grn_id`.

    Args:
        grn_id (int): The unique identifier of the GRN to be retrieved.
        db (Session): SQLAlchemy database session dependency.

    Returns:
        list[GRNRead]: A list containing the GRN record(s) that match the given ID.
    """
    return db.query(GRN).filter(GRN.id == grn_id).all()



@router.get("/get_grn", response_model=list[GRNRead])
def get_grns(
    GRN_No: int = Query(None),
    from_date: str = Query(None),  # Accept as string/timestamp
    to_date: str = Query(None),
    page: int = Query(1, ge=1),
    page_size:int=Query(10,ge=10),
    db: Session = Depends(get_db)
):
    """
    Retrieve GRN records.

    - If `GRN_No`, `from_date`, and `to_date` are provided → returns filtered records.
    - Else → returns paginated records (10 per page).
    """
    def parse_date(value):
        if not value:
            return None
        try:
            # Case: timestamp in milliseconds or seconds
            if value.isdigit():
                ts = int(value)
                if ts > 1e12:  # milliseconds
                    ts //= 1000
                return datetime.fromtimestamp(ts).date()
            # Case: ISO date string
            return datetime.fromisoformat(value).date()
        except Exception:
            raise HTTPException(status_code=400, detail=f"Invalid date format: {value}")

    from_date_parsed = parse_date(from_date)
    to_date_parsed = parse_date(to_date)

    page_size = page_size
    offset = (page - 1) * page_size

    if GRN_No is not None and from_date_parsed and to_date_parsed:
        grns = (
            db.query(GRN)
            .filter(
                GRN.id == GRN_No,
                GRN.invoice_date.between(from_date_parsed, to_date_parsed)
            )
            .offset(offset)
            .limit(page_size)
            .all()
        )
    else:
        grns = db.query(GRN).offset(offset).limit(page_size).all()

    if not grns:
        raise HTTPException(status_code=404, detail="No GRN records found")

    return grns



@router.put("/{grn_id}", response_model=GRNRead)
def update_grn(grn_id: int, product: GRNCreate, db: Session = Depends(get_db)):
    """
    Update an existing GRN (Goods Receipt Note) record by ID.

    This endpoint updates both the main GRN details and its associated medicines.
    The existing medicines will be removed and replaced with the provided list.

    Args:
        grn_id (int): The unique ID of the GRN to update.
        product (GRNCreate): The updated GRN data including medicines.
        db (Session, optional): The database session dependency.

    Raises:
        HTTPException: If no GRN is found with the given `grn_id` (404 Not Found).

    Returns:
        GRNRead: The updated GRN record with all its details and medicines.
    """
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
