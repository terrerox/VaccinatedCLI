import webbrowser
from src.province.province_model import Province
from src.helpersLib.helpers import *

class ProvinceService:

    def add():
        clear()
        try:
            cancel = input(color.CYAN + 'Registrar una provincia (Presione ENTER para continuar) // Digite X para cancelar: ')
            if cancel == "x" or cancel == "X":
                return False
            newProvince = Province()
            newProvince.name = input('Digite el nombre: ')
            newProvince.save()
            input('Provincia registrada')
        except Exception as e:
            input(e)
            
    def update():
        clear()
        print(showProvinces())
        try:
            idx = input(color.YELLOW + 'Coloca el id de la provincia a modificar // Digite X para cancelar: ')
            if idx == "x" or idx == "X":
                return False
            updateProvince = Province.select().where(Province.id == idx).get()
            updateProvince.name = confirmData('Nombre', updateProvince.name)
            updateProvince.save()
            input('Provincia actualizada con éxito')
        except:
            input(color.RED +'Ocurrió un error repita el proceso. ')

    def delete():
        clear()
        try:
            print(showProvinces())
            idx = input(color.MAGENTA + 'Digita el ID de la que quieras eliminar // Digite X para cancelar: ')
            if idx == "x" or idx == "X":
                return False
            if Province.delete_by_id(idx):
                input('La provincia ha sido eliminada con éxito')
            else:
                input('Id digitado no existe')
        except:
            input(color.RED +'Ocurrió un problema, intentelo nuevamente')
            input('error')