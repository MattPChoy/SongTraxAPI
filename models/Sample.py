from sqlalchemy import Column, Integer, String
from models.Base import Base


class Sample(Base):
    __tablename__ = "Sample"

    id = Column(Integer, primary_key=True, index=True)
    apiKey = Column(String)
    name = Column(String)
    recordingData = Column(String)
