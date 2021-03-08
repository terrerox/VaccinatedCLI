import webbrowser
from src.vaccine.vaccine_model import Vaccine
from src.helpersLib.helpers import *

class VaccineService:

    def add():
        clear()
        try:
            cancel = input(color.CYAN + 'Registrar una vacuna (Presione ENTER para continuar) // Digite X para cancelar: ')
            if cancel == "x" or cancel == "X":
                return False
            newVaccine = Vaccine()
            newVaccine.name = input('Digite el nombre: ')
            newVaccine.save()
            input('Vacuna registrada')
        except Exception as e:
            input(e)
            
    def update():
        clear()
        print(showVaccines())
        try:
            idx = input(color.YELLOW + 'Coloca el id de la vacuna a modificar // Digite X para cancelar: ')
            if idx == "x" or idx == "X":
                return False
            updateVaccine = Vaccine.select().where(Vaccine.id == idx).get()
            updateVaccine.name = confirmData('Nombre', updateVaccine.name)
            updateVaccine.save()
            input('Vacuna actualizada con éxito')
        except:
            input(color.RED +'Ocurrió un error repita el proceso. ')

    def delete():
        clear()
        try:
            print(showVaccines())
            idx = input(color.MAGENTA + 'Digita el ID de la que quieras eliminar // Digite X para cancelar: ')
            if idx == "x" or idx == "X":
                return False
            if Vaccine.delete_by_id(idx):
                input('La vacuna ha sido eliminada con éxito')
            else:
                input('Id digitado no existe')
        except:
            input(color.RED +'Ocurrió un problema, intentelo nuevamente')