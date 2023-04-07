from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# 1 getting a schedule
class GetSchedule(BaseModel):
    start_date: datetime
    end_date: datetime


# 2 getting client info
class GetClient(BaseModel):
    client_first_name: str
    client_last_name: str


# 3 getting trainer info
class GetTrainer(BaseModel):
    trainer_first_name: str
    trainer_last_name: str


# 4 setting a schedule
class PostSchedule(BaseModel):
    start_date: datetime
    end_date: datetime
    client_first_name: str
    client_last_name: str
    trainer_first_name: str
    trainer_last_name: str


# 5 updating a schedule
class UpdateSchedule(BaseModel):
    id: UUID
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    client_first_name: Optional[str]
    client_last_name: Optional[str]
    trainer_first_name: Optional[str]
    trainer_last_name: Optional[str]
