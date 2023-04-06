from datetime import datetime

from pony.orm import Database, Required, Set

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Schedule(db.Entity):
    start_date = Required(datetime)
    end_date = Required(datetime)
    trainer = Required("Trainer")
    client = Required("Client")


class Client(db.Entity):
    first_name = Required(str)
    last_name = Required(str)
    schedules = Set("Schedule")


class Trainer(db.Entity):
    first_name = Required(str)
    last_name = Required(str)
    schedules = Set("Schedule")
