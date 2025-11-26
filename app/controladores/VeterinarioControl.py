from app.vista.VeterinarioVista import VeterinarioVista
from app.modelos.Veterinario import Veterinario

class VeterinarioControl:
    def __init__(self, conexionContexto):
        self.conexionContexto = conexionContexto
        self.veterinarioVista = VeterinarioVista()

    def ejecutar(self):
        accionUsuario = self.veterinarioVista.veterinarioMenu()

        if accionUsuario == "1":
            self.crearVeterinario()
        elif accionUsuario == "2":
            self.leerVeterinario()
        elif accionUsuario == "3":
            self.actualizarVeterinario()
        elif accionUsuario == "4":
            self.eliminarVeterinario()
        elif accionUsuario == "5":
            pass
        else:
            print("\n Ingrese valor valido ")


    def crearVeterinario(self):
        print("\n    Creacion Veterinario")
        rut = input("Ingrese rut del veterinario: ")
        nombre = input("Ingrese nombre: ")
        especialidad = input("Ingrese especialidad: ")
        anios = input("Ingrese años de experiencia: ")
        contacto = input("Ingrese contacto: ")

        vet = Veterinario(rut, nombre, especialidad, anios, contacto)
        self.conexionContexto.VeterinarioRepo.crearVeterinario(vet)
        print("\Acción realizada con éxito, buen dia.")

    def leerVeterinario(self):
        print("\n     Lectura de Veterinarios")

        self.conexionContexto.VeterinarioRepo.leerVeterinario() 

    def actualizarVeterinario(self):
        print("\n        Actualizacion Veterinario")
        rut = input("\nIngrese rut de Veterinario: ")
        
        print(
                 "Dato a modificar: \n" \
        "1. Nombre\n" \
        "2. Especialidad\n" \
        "3. Años de experiencia\n" \
        "4. Contacto"
        )

        accionUsuario = input("\nIngrese opcion: ")
        
        if accionUsuario == "1":
            variableModificar = "nombre"
        elif accionUsuario == "2":
            variableModificar = "especialidad"
        elif accionUsuario == "3":
            variableModificar = "anios_experiencia"
        elif accionUsuario == "4":
            variableModificar = "contacto"
        else:
            print("\nIngrese opcion valida")
            return
        
        nuevoDato = input("\nIngrese el nuevo dato: ")

        self.conexionContexto.VeterinarioRepo.actualizarVeterinario(rut, variableModificar, nuevoDato)

        print("\Acción realizada con éxito, buen dia.")  

        
    def eliminarVeterinario(self):
        print("\n     Eliminar Veterinario")
        rut = input("\nIngrese rut de veterinario: ")

        self.conexionContexto.VeterinarioRepo.eliminarVeterinario(rut)

        print("\Acción realizada con éxito, buen dia.")