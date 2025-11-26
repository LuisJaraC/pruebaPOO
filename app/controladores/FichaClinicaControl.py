from app.vista.FichaClinicaVista import FichaClinicaVista
from app.modelos.FichaClinica import FichaClinica

class FichaClinicaControl:
    def __init__(self, conexionContexto):
        self.conexionContexto = conexionContexto

        self.fichaVista = FichaClinicaVista()

    def ejecutar(self):
        accionUsuario = self.fichaVista.fichaMenu()

        if accionUsuario == "1":
            self.crearFichaClinica()
        elif accionUsuario == "2":
            self.leerFicha()
        elif accionUsuario == "3":
            self.actualizarFicha()
        elif accionUsuario == "4":
            self.eliminarFicha()
        elif accionUsuario == "5":
            pass
        else:
            print("\n Ingrese valor valido ")       

    def crearFichaClinica(self):
        print("\n    Creacion Ficha Clinica")
        id_mascota = input("Ingrese id_mascota: ")
        diagnostico = input("Ingrese diagnostico: ")
        tratamiento = input("Ingrese tratamiento: ")
        restricciones = input("Ingrese restricciones: ")
        

        fichaCli = FichaClinica(id_mascota, diagnostico, tratamiento, restricciones)

        self.conexionContexto.FichaClinicaRepo.crearFichaClinica(fichaCli)

        print("\Acción realizada con éxito, buen dia.")

    def leerFicha(self):
        print("\n     Lectura de Fichas")

        self.conexionContexto.FichaClinicaRepo.leerFicha()

    def actualizarFicha(self):
        print("\n        Actualizacion de Fichas")
        id_ficha = input("\nIngrese id_ficha: ")
        print(
                 "Dato a modificar: \n" \
        "1. id mascota\n" \
        "2. fecha de creacion\n" \
        "3. diagnostico\n" \
        "4. tratamientos\n" \
        "5. restricciones"
        )
        accionUsuario = input("\nIngrese opcion: ")
        if accionUsuario == "1":
            variableModificar = "id_mascota"
        elif accionUsuario == "2":
            variableModificar = "fecha_creacion"
        elif accionUsuario == "3":
            variableModificar = "diagnostico"
        elif accionUsuario == "4":
            variableModificar = "Tratamientos"
        elif accionUsuario == "5":
            variableModificar = "Restricciones_alertas"
        else:
            print("\nIngrese opcion valida")
            return
        
        nuevoDato = input("\nIngrese el nuevo dato: ")
        self.conexionContexto.FichaClinicaRepo.actualizarFicha(id_ficha,variableModificar,nuevoDato)
        print("\Acción realizada con éxito, buen dia.")
    
    def eliminarFicha(self):
        print("\n     Eliminar Ficha")
        id_ficha = input("\nIngrese el id de la ficha: ")
        self.conexionContexto.FichaClinicaRepo.eliminarFicha(id_ficha)
        print("\Acción realizada con éxito, buen dia.")
        
