from app.vista.ProcedimientoVista import ProcedimientoVista
from app.modelos.Procedimiento import Procedimiento

class ProcedimientoControl:
    def __init__(self, conexionContexto):
        self.conexionContexto = conexionContexto

        self.procedimientoVista = ProcedimientoVista()

    def ejecutar(self):
        accionUsuario = self.procedimientoVista.procedimientoMenu()
        
        if accionUsuario == "1":
            self.crearProcedimiento()
        elif accionUsuario == "2":
            self.leerProcedimiento()
        elif accionUsuario == "3":
            self.actualizarProcedimiento()
        elif accionUsuario == "4":
            self.eliminarProcedimiento()
        elif accionUsuario == "5":
            pass
        else:
            print("\n Ingrese valor valido ")


    def crearProcedimiento(self):
        print("\n       Creacion Procedimiento")
        id_ficha = input("ID Ficha: ")
        rut_vet = input("RUT Veterinario: ")
        tipo = input("Tipo Proc: ")
        indicaciones = input("Indicaciones: ")
        costo = input("Costo: ")

        # Instanciamos SIN pasar ID ni Fecha (automáticamente serán None)
        procedimiento = Procedimiento(id_ficha, rut_vet, tipo, indicaciones, costo)
    
        self.conexionContexto.ProcedimientoRepo.crearProcedimiento(procedimiento)

        print("\Acción realizada con éxito, buen dia.")

    def leerProcedimiento(self):
        print("\n     Lectura de Procedimiento")

        self.conexionContexto.ProcedimientoRepo.leerProcedimiento()

    def actualizarProcedimiento(self):
        print("\n        Actualizacion Procedimiento")
        id_procedimiento = input("\nIngrese id procedimiento: ")
        
        print(
                 "Dato a modificar: \n" \
        "1. Tipo de Procedimiento\n" \
        "2. Indicaciones\n" \
        "3. Costo\n" \
        "4. Rut veterinario ( debe existir)"
        )

        accionUsuario = input("\nIngrese opcion: ")
        
        if accionUsuario == "1":
            variableModificar = "tipo_procedimiento"
        elif accionUsuario == "2":
            variableModificar = "indicaciones"
        elif accionUsuario == "3":
            variableModificar = "costo"
        elif accionUsuario == "4":
            variableModificar = "rut_veterinario"
        else:
            print("\nIngrese opcion valida")
            return
        
        nuevoDato = input("\nIngrese el nuevo dato: ")

        self.conexionContexto.ProcedimientoRepo.actualizarProcedimiento(id_procedimiento, variableModificar, nuevoDato)

        print("\Acción realizada con éxito, buen dia.")

    def eliminarProcedimiento(self):
        print("\n     Eliminar Procedimiento")
        id_procedimiento = input("\nIngrese id de procedimiento: ")

        self.conexionContexto.ProcedimientoRepo.eliminarProcedimiento(id_procedimiento)

        print("\Acción realizada con éxito, buen dia.")