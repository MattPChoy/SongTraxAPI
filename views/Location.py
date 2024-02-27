from fastapi import APIRouter
from sqlalchemy.orm import Session, sessionmaker

from models.Location import Location
from models.LocationDTO import LocationDTO

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

router = APIRouter(
    prefix="/location",
)

@router.get("/")
def get_location(apiKey: str):
    db: Session = SessionLocal()

    entries = db.query(Location).filter(Location.apiKey == apiKey).all()
    return entries

@router.post("/")
def create_location(location: LocationDTO):
    db: Session = SessionLocal()
    location = Location(
        apiKey=location.apiKey,
        name=location.name,
        latitude=location.latitude,
        longitude=location.longitude,
        sharing=location.sharing
    )
    db.add(location)
    db.commit()
    # Update to reflect changes in the DB, such as the ID
    db.refresh(location) 
    return location