
from fastapi import APIRouter, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
import pandas as pd
from datetime import datetime
from io import BytesIO
from datetime import datetime
import os
from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
router = APIRouter(prefix="/importexcel", tags=["ImportExcel"])



MEDIA_FOLDER = "media"
@router.post("/")
async def importexcel(file: UploadFile):
    """  import excel file and read projects insode upload folder read data and validated each every field """
    
    # Validate file format
    if not file.filename.endswith((".xlsx", ".xls", ".csv")):
        raise HTTPException(status_code=400, detail="Invalid file format")

    # Save file
    os.makedirs(MEDIA_FOLDER, exist_ok=True)
    file_path = os.path.join(MEDIA_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Read file into DataFrame
    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading file: {str(e)}")

    # Expected columns and types
    expected_columns = {
        "Sl No": "int",
        "Medicine Name": "string",
        "Exp.Date": "date",
        "Batch No": "string",
        "Received Qty": "int",
        "Free Qty": "int",
        "Sheet Qty": "int",
        "QOH": "int",
        "Unit": "string",
        "Pack Cost": "float",
        "Disc (%)": "float",
        "Total Amt": "float",
        "CGST%": "float",
        "SGST%": "float",
        "IGST%": "float",
        "Tab MRP": "float"
    }

    # Check missing columns
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        raise HTTPException(status_code=400, detail=f"Missing required columns: {', '.join(missing_columns)}")

    # Data type validation
    errors = []
    for col, dtype in expected_columns.items():
        for i, value in enumerate(df[col], start=1):
            if pd.isna(value):
                errors.append(f"Row {i}, Column '{col}' is empty")
                continue

            if dtype == "int":
                if not isinstance(value, (int, float)) or pd.isna(value) or int(value) != value:
                    errors.append(f"Row {i}, Column '{col}' must be an integer")
            elif dtype == "float":
                if not isinstance(value, (int, float)):
                    errors.append(f"Row {i}, Column '{col}' must be a number")
            elif dtype == "string":
                if not isinstance(value, str):
                    errors.append(f"Row {i}, Column '{col}' must be text")
            elif dtype == "date":
                try:
                    if not isinstance(value, datetime):
                        datetime.strptime(str(value), "%Y-%m-%d")
                except ValueError:
                    try:
                        datetime.strptime(str(value), "%d-%m-%Y")
                    except ValueError:
                        errors.append(f"Row {i}, Column '{col}' must be a valid date (YYYY-MM-DD or DD-MM-YYYY)")

    if errors:
        raise HTTPException(status_code=400, detail=errors)

    return {"message": "File uploaded and validated successfully"}

