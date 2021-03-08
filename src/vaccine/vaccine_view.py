import os
from src.helpersLib.helpers import clear, color
from src.vaccine.vaccine_service import VaccineService

class VaccineView():

    def start():
        choosing = True
        while choosing:
            clear()
            print(color.WHITE + """
            Administra las vacunas
            1- Agregar
            2- Modificar
            3- Eliminar 
            4- Atrás
            """)
            option = input('Digite la opción que prefiera: ')
            if option == '1':
                VaccineService.add()
            elif option == '2':
                VaccineService.update()
            elif option == '3':
                VaccineService.delete()
            elif option == '4':
                choosing = False
            else:
                input('Opción no encontrada')