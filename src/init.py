import os
from src.helpersLib.helpers import color
from src.settings import Settings
from src.patient.patient_service import PatientService

class Init():

    def start():
        choosing = True
        while choosing:
            os.system('cls')
            print(color.BLUE + """

            Aplicación de Vacunas       

            """)
            print(color.WHITE + """
            1- Registrar vacunado
            2- Exportar
            3- Configuración 
            4- Salir
            """)
            option = input('Digite la opción que prefiera: ')
            if option == '1':
                PatientService.add()
            elif option == '2':
                PatientService.export()
            elif option == '3':
                Settings.start()
            elif option == '4':
                choosing = False
            else:
                input(color.RED + 'Elija una opción existente')