from fastapi import APIRouter
from sqlalchemy.orm import Session, sessionmaker

from models.SampleToLocation import SampleToLocation
from models.SampleToLocationDTO import SampleToLocationDTO

from data.dataContext import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

router = APIRouter(
    prefix="/sampleToLocation",
)

@router.get("/")
def get_sample_to_location(apiKey: str):
    db: Session = SessionLocal()

    entries = db.query(SampleToLocation).filter(SampleToLocation.apiKey == apiKey).all()
    return entries

@router.post("/")
def create_sample_to_location(sampleToLocation: SampleToLocationDTO):
    db: Session = SessionLocal()
    sampleToLocation = SampleToLocation(
        apiKey=sampleToLocation.apiKey,
        sampleId=sampleToLocation.sampleId,
        locationId=sampleToLocation.locationId
    )
    db.add(sampleToLocation)
    db.commit()
    # Update to reflect changes in the DB, such as the ID
    db.refresh(sampleToLocation)
    return sampleToLocation