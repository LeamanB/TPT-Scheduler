from datetime import datetime
from uuid import UUID

from pony.orm import Database, Required, Set, PrimaryKey

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Schedule(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    start_date = Required(datetime)
    end_date = Required(datetime)
    trainer = Required("Trainer")
    client = Required("Client")


class Client(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    first_name = Required(str)
    last_name = Required(str)
    schedules = Set("Schedule")


class Trainer(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    first_name = Required(str)
    last_name = Required(str)
    schedules = Set("Schedule")

db.generate_mapping(create_tables=True)