from pydantic import BaseModel
from typing import Optional

class SampleDTO(BaseModel):
    apiKey: str
    name: str
    recordingData: str
