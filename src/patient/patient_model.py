from peewee import CharField, DateField, Model, IntegerField, ForeignKeyField
from src.config.config import db
from src.province.province_model import Province
from src.vaccine.vaccine_model import Vaccine

class Patient(Model):
    code = IntegerField(unique=True)
    name = CharField(50)
    lastName = CharField(50)
    telNumber = CharField(50) 
    birthDate = DateField()
    vaccine = ForeignKeyField(Vaccine, backref='vaccine')
    province = ForeignKeyField(Province, backref='province')
    firstDoseDate = DateField()
    secondDoseDate = DateField(null = True)

    class Meta: 
        database = db

db.create_tables([Patient])