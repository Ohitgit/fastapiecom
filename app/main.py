from fastapi import FastAPI
from app.database import Base, engine
from app.models import category, product
from app.routers import suplier as suplier_router, pharmacy as pharmacy_router , invoice as invoice_router,invoicemultiple as invoicemultiple_router

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product & Category & Suplier API ")

# Include routers

app.include_router(suplier_router.router)
app.include_router(pharmacy_router.router)
app.include_router(invoice_router.router)
app.include_router(invoicemultiple_router.router)
