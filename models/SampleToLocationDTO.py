from pydantic import BaseModel

class SampleToLocationDTO(BaseModel):
    sampleId: int
    locationId: int