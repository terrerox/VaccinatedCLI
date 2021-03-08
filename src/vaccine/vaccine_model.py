from peewee import CharField, Model
from src.config.config import db

class Vaccine(Model):
    name = CharField(50)

    class Meta: 
        database = db

db.create_tables([Vaccine])