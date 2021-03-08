import webbrowser
from src.patient.patient_model import Patient
from src.helpersLib.helpers import *

class PatientService:

    def add():
        clear()
        try:
            cancel = input(color.CYAN + 'Registrar un vacunado (Presione ENTER para continuar) // Digite X para cancelar: ')
            if cancel == "x" or cancel == "X":
                return False

            code = input('Digite su cédula: ')
            if getPatientByCode(code):
                print(color.GREEN + 'El vacunado ya está registrado, proceda a agregarle la fecha de la segunda dósis')
                currentPatient = getPatientByCode(code)
                currentPatient.secondDoseDate =  formatDate(input(color.CYAN + 'Digite la fecha de la segunda dósis en formato Y-M-D: '))
                currentPatient.save()
                input(color.GREEN + 'Segunda dósis guardada')
            else:
                newPatient = Patient()
                newPatient.code = code
                newPatient.name = input('Digite el nombre: ')
                newPatient.lastName = input('Digite la apellido: ')
                newPatient.telNumber = input('Digite el número de telefono: ')
                newPatient.birthDate = formatDate(input('Digite la fecha de nacimiento en formato Y-M-D: '))
                print(showVaccines())
                newPatient.vaccine = input('Digite el ID de la vacuna: ')
                print(showProvinces())
                newPatient.province = input('Digite el ID de la provincia: ')
                newPatient.firstDoseDate = formatDate(input('Digite la fecha de la primera dósis en formato Y-M-D: '))
                newPatient.save()
                input(color.GREEN + 'Paciente registrado')
        except:
            input(color.RED + 'Ocurrió un error, verifique sus datos.')

    def export():
        data = showPatients()
        table = data.get_html_string()
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="style.css">
            <title>Vacunados</title>
        </head>
        <body>
            <div class="container">
                <h1 class="title">Reporte de Vacunados</h1>
                {table}
            </div>
        </body>
        </html>
        """
        f = open('vacunados.html','w', encoding="utf-8")
        f.write(html)
        f.close()
        webbrowser.open('vacunados.html')