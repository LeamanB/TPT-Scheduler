from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException
from pony.orm import commit

from database import Schedule, Client, Trainer
from schema import PostSchedule, UpdateSchedule, PostTrainer, PostClient

app = FastAPI()


@app.get("/schedule/")
async def get_schedule(id: UUID):
    return Schedule.get(id=id)


@app.get("/client/")
async def get_client(id: UUID):
    return Client.get(id=id)


@app.get("/trainer/")
async def get_trainer(id:UUID):
    return Trainer.get(id=id)


@app.post("/schedule/")
async def create_schedule(schedule: PostSchedule):
    client = Client.get(id=schedule.client_id)
    trainer = Trainer.get(id=schedule.trainer_id)
    data = schedule.dict()
    data.pop("client_id")
    data.pop("trainer_id")
    schedule = Schedule(client=client, trainer=trainer, **data)
    commit()
    return schedule.id

@app.post("/client/")
async def create_client(client: PostClient):
    data = client.dict()
    client = Client(**data)
    commit()
    return client.id

@app.post("/trainer/")
async def create_trainer(trainer: PostTrainer):
    data = trainer.dict()
    trainer = Trainer(**data)
    commit()
    return trainer.id

@app.put("/schedule/")
async def update_schedule(schedule: UpdateSchedule):
    schedule_ = Schedule.get(id=schedule.id)
    schedule_.set(**schedule.dict(exclude_unset=True))
    commit()
    return schedule_


@app.get("/schedules/")
async def get_lists_of_schedule(ids: list[str]):
    return Schedule.get(id=id)


@app.get("/clients/")
async def get_lists_of_clients(ids: list[str]):
    return Client.get(id=id)
    # todo
