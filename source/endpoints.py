from uuid import uuid4, UUID

from fastapi import FastAPI, HTTPException

from database import Schedule, Client, Trainer
from schema import PostSchedule, UpdateSchedule

app = FastAPI()


# endpoints

# 1 getting a schedule
@app.get("/schedule/")
async def get_schedule(id: UUID):
    return Schedule.get(id=id)


# 2 getting client info
@app.get("/client/")
async def get_client(id: UUID,):
    return Client.get(id=id)


# 3 getting trainer info
@app.get("/trainer/")
async def get_trainer(id:UUID):
    return Trainer.get(id=id)


# 4 setting a schedule
@app.post("/schedule/")
async def create_schedule(schedule: PostSchedule):
    uuid = uuid4()
    schedules[uuid] = schedule.dict()
    return uuid


# 5 updating a schedule
@app.put("/schedule/")
async def update_schedule(schedule: UpdateSchedule):
    try:
        schedules[schedule.id].update(schedule.dict())
    except KeyError:
        raise HTTPException(status_code=404, detail="wrong id")


# 6 getting several schedules
@app.get("/schedules/")
async def get_lists_of_schedule(ids: list[str]):
    return Schedule.get(id=id)


# 7 getting several clients
@app.get("/clients/")
async def get_lists_of_clients(ids: list[str]):
    return Client.get(id=id)
    # todo
