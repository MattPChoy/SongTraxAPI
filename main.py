from sqlalchemy import create_engine
from models.Base import Base
from models.Location import Location
from models.SampleRating import SampleRating
from models.SampleToLocation import SampleToLocation

from views.Sample import router as sampleRouter

from fastapi import FastAPI

engine = create_engine('sqlite:///./database.db')
Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(sampleRouter)