import os
from src.helpersLib.helpers import color
from src.patient.patient_service import PatientService
from src.vaccine.vaccine_view import VaccineView
from src.province.province_view import ProvinceView

class Settings():

    def start():
        choosing = True
        while choosing:
            os.system('cls')
            print(color.WHITE + """
                    Configuración
                    1- Vacunas
                    2- Provincias
                    3- Atrás
                    """)
            option = input('Digite la opción que prefiera: ')
            if option == '1':
                VaccineView.start()
            elif option == '2':
                ProvinceView.start()
            elif option == '3':
                choosing = False
            else:
                input('optionNotFound')
