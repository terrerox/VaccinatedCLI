import os
from src.helpersLib.helpers import clear, color
from src.province.province_service import ProvinceService

class ProvinceView():

    def start():
        choosing = True
        while choosing:
            clear()
            print(color.WHITE + """
            Administra las provincias
            1- Agregar
            2- Modificar
            3- Eliminar 
            4- Atrás
            """)
            option = input('Digite la opción que prefiera: ')
            if option == '1':
                ProvinceService.add()
            elif option == '2':
                ProvinceService.update()
            elif option == '3':
                ProvinceService.delete()
            elif option == '4':
                choosing = False
            else:
                input('Opción no encontrada')