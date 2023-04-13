from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class GetSchedule(BaseModel):
    start_date: datetime
    end_date: datetime


class GetClient(BaseModel):
    first_name: str
    last_name: str


class GetTrainer(BaseModel):
    first_name: str
    last_name: str


class PostSchedule(BaseModel):
    start_date: datetime
    end_date: datetime
    client_id: UUID
    trainer_id: UUID


class PostClient(BaseModel):
    first_name: str
    last_name: str


class PostTrainer(BaseModel):
    first_name: str
    last_name: str


class UpdateSchedule(BaseModel):
    id: UUID
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    client_id: UUID
    trainer_id: UUID


class UpdateClient(BaseModel):
    id: UUID
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    client_id: UUID
    trainer_id: UUID


class UpdateTrainer(BaseModel):
    id: UUID
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    client_id: UUID
    trainer_id: UUID
