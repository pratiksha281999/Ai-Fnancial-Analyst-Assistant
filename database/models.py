from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from database.db import Base


class Portfolio(Base):
    __tablename__ = "portfolio"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    quantity = Column(Integer)
    buy_price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
