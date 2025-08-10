from sqlalchemy import Column, Integer, String
from app.database import Base
class Suplier(Base):
      __tablename__= "supliers"
      
      id = Column(Integer, primary_key=True, index=True)
      name =Column(String(128),nullable=True)