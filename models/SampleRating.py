from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import mapped_column

from models.Base import Base
from models.Sample import Sample


class SampleRating(Base):
    __tablename__ = "SampleRating"

    id = Column(Integer, primary_key=True, index=True)
    sampleId = mapped_column(Integer, ForeignKey(Sample.id))
    rating = Column(Integer)
