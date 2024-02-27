from sqlalchemy import Boolean, Column, Integer, String, Float

from models.Base import Base


class Location(Base):
    __tablename__ = "Location"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    sharing = Column(Boolean)
