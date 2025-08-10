from sqlalchemy import Column, Integer, String
from app.database import Base
class Pharmacy(Base):
      __tablename__= "pharmacys"

      id = Column(Integer, primary_key=True, index=True)
      name =Column(String(128),nullable=True)
