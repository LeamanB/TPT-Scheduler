from uuid import UUID

from fastapi import FastAPI, HTTPException
from pony.orm import commit, select

from database import Schedule, Client, Trainer
from schema import PostSchedule, UpdateSchedule, UpdateTrainer, UpdateClient, PostTrainer, PostClient

app = FastAPI()


@app.get("/schedule/")
async def get_schedule(id: UUID):
    schedule = Schedule.get(id=id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule


@app.get("/client/")
async def get_client(id: UUID):
    client = Client.get(id=id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@app.get("/trainer/")
async def get_trainer(id: UUID):
    trainer = Trainer.get(id=id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return trainer


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
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule_.to_dict()


@app.put("/trainer/")
async def update_trainer(trainer: UpdateTrainer):
    trainer_ = Trainer.get(id=trainer.id)
    trainer_.set(**trainer.dict(exclude_unset=True))
    commit()
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return trainer_.to_dict()


@app.put("/client/")
async def update_client(client: UpdateClient):
    client_ = Client.get(id=client.id)
    if not client_:
        raise HTTPException(status_code=404, detail="Client not found")
    client_.set(**client.dict(exclude_unset=True))
    return client_.to_dict()


@app.get("/schedules/")
async def get_schedules(skip: int = 0, limit: int = 10):
    schedules = select(i for i in Schedule).order_by(Schedule.id).limit(limit, offset=skip)[:]
    return [schedule.to_dict() for schedule in schedules]


@app.get("/clients/")
async def get_clients(skip: int = 0, limit: int = 10):
    clients = select(i for i in Client).order_by(Client.id).limit(limit, offset=skip)[:]
    return [client.to_dict() for client in clients]


@app.get("/trainers/")
async def get_trainers(skip: int = 0, limit: int = 10):
    trainers = select(i for i in Trainer).order_by(Client.id).limit(limit, offset=skip)[:]
    return [trainer.to_dict() for trainer in trainers]