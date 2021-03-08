import os
import winsound
from datetime import datetime
from src.patient.patient_model import Patient
from src.vaccine.vaccine_model import Vaccine
from src.province.province_model import Province
from prettytable import PrettyTable 

def getPatientByCode(code):
    try:
        currentPatient = Patient.select().where(Patient.code == code).get()
        return currentPatient
    except:
        return False

def formatDate(date):
    date = datetime.strptime(date, "%Y-%m-%d") 
    return date

def clear():
    os.system('cls')

def showPatients():
    query = (Patient
         .select()
         .join(Vaccine, on=(Vaccine.id == Patient.vaccine))
         .join(Province, on=(Province.id == Patient.province)))

    tbl = PrettyTable()
    tbl.field_names = ["id", "Cedula", "Nombre","Apellido", "Teléfono", "Fecha de nacimiento", "Vacuna", "Provincia", "Fecha de primera dósis", "Fecha de segunda dósis"]
    for pat in query:
        tbl.add_row([pat.id, pat.code, pat.name, pat.lastName, pat.telNumber, pat.birthDate, pat.vaccine.name, pat.province.name, pat.firstDoseDate, pat.secondDoseDate])
    return tbl

def showVaccines():
    tbl = PrettyTable()
    tbl.field_names = ["id", "Nombre"]
    for vaccine in Vaccine.select():
        tbl.add_row([vaccine.id, vaccine.name])
    return tbl

def showProvinces():
    tbl = PrettyTable()
    tbl.field_names = ["id", "Nombre"]
    for province in Province.select():
        tbl.add_row([province.id, province.name])
    return tbl

def confirmData(field, value):
    print(f'El campo {field} tiene el valor {value}')
    tmp = input('Digite el nuevo valor o dejelo en blanco para no cambiar: ')
    if tmp == '':
        return value
    else: 
        return tmp

class color():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'