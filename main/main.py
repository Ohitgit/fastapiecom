from fastapi import FastAPI
from main.database import Base, engine
from main.models  import grn ,grnmedicine

from main.routers import importexcel as import_excel_router ,grn as grn_router,grnmedicine as grnmedicine_router
# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="GRN & GRN Medicine API ")

# Include routers

app.include_router(import_excel_router.router)
app.include_router(grn_router.router)
# app.include_router(grnmedicine_router.router)
