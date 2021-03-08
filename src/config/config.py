from peewee import  SqliteDatabase

db = SqliteDatabase('vaccines.db', pragmas={'foreign_keys': 1})
db.connect()