from fastapi import APIRouter
from sqlalchemy.orm import Session, sessionmaker

from models.Sample import Sample
from models.SampleDTO import SampleDTO

from data.dataContext import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

router = APIRouter(
    prefix="/sample",
)

@router.get("/")
def get_sample(apiKey: str):
    db: Session = SessionLocal()

    entries = db.query(Sample).filter(Sample.apiKey == apiKey).all()
    return entries

@router.post("/")
def create_sample(sample: SampleDTO):
    db: Session = SessionLocal()
    sample = Sample(
        apiKey=sample.apiKey,
        name=sample.name,
        recordingData=sample.recordingData
    )
    db.add(sample)
    db.commit()
    # Update to reflect changes in the DB, such as the ID
    db.refresh(sample) 
    return sample