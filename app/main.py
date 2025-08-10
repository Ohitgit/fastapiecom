from fastapi import FastAPI
from app.database import Base, engine
from app.models import category, product
from app.routers import category as category_router, product as product_router

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product & Category API")

# Include routers
app.include_router(category_router.router)
app.include_router(product_router.router)
