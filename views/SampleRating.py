from fastapi import APIRouter
from sqlalchemy.orm import Session, sessionmaker

from models.SampleRating import SampleRating
from models.SampleRatingDTO import SampleRatingDTO

from data.dataContext import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

router = APIRouter(
    prefix="/sampleRating",
)

@router.get("/")
def get_sample_rating(apiKey: str):
    db: Session = SessionLocal()

    entries = db.query(SampleRating).filter(SampleRating.apiKey == apiKey).all()
    return entries

@router.post("/")
def create_sample_rating(sampleRating: SampleRatingDTO):
    # TODO: Check FK constraint
    db: Session = SessionLocal()
    sampleRating = SampleRating(
        apiKey=sampleRating.apiKey,
        sampleId=sampleRating.sampleId,
        rating=sampleRating.rating
    )
    db.add(sampleRating)
    db.commit()
    # Update to reflect changes in the DB, such as the ID
    db.refresh(sampleRating) 
    return sampleRating