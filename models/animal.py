from pydantic import BaseModel, Field
from typing import Optional


class Animal(BaseModel):
    animal_breed: str
    animal_description: Optional[str]
    average_size: Optional[int] = Field(gt=10)

