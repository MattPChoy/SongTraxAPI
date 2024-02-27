from pydantic import BaseModel
from typing import Optional

class SampleRatingDTO(BaseModel):
    sampleId: int
    rating: int
