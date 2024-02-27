from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import mapped_column

from models.Base import Base
from models.Sample import Sample
from models.Location import Location


class SampleToLocation(Base):
    __tablename__ = "SampleToLocation"

    id = Column(Integer, primary_key=True, index=True)
    sampleId = mapped_column(Integer, ForeignKey(Sample.id))
    locationId = mapped_column(Integer, ForeignKey(Location.id))
