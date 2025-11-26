from app.vista.CuidadorVista import CuidadorVista
from app.modelos.Cuidador import Cuidador

class CuidadorControl:
    def __init__(self, conexionContexto):
        self.conexionContexto = conexionContexto

        # se inicializan vista para acceder a sus metodos
        self.cuidadorVista = CuidadorVista()
        

    def ejecutar(self):
        accionUsuario = self.cuidadorVista.cuidadorMenu()
        
        if accionUsuario == "1":
            self.crearCuidador()
        elif accionUsuario == "2":
            self.leerCuidador()
        elif accionUsuario == "3":
            self.actualizarCuidador()
        elif accionUsuario == "4":
            self.eliminarCuidador()
        elif accionUsuario == "5":
            pass
        else:
            print("\n Ingrese valor valido ")



    def crearCuidador(self):
        # Pedimos datos, instanciamos Cuidador para luego enviarlo al repo correspondiente
        print("\n    Creacion Cuidador")
        rut = input("Ingrese rut: ")
        nombre = input("Ingrese nombre: ")
        direccion = input("Ingrese direccion: ")
        telefono = input("Ingrese telefono: ")
        email = input("Ingrese email: ")

        cuidador = Cuidador(rut, nombre, direccion, telefono, email)

        # Utilizamos la conexionContexto que contiene como atributos los sub-repos inicializados
        # Por lo tanto podemos acceder a los metodos de los sub-repos.
        self.conexionContexto.CuidadorRepo.crearCuidador(cuidador)

        print("\Acción realizada con éxito, buen dia.")

    def leerCuidador(self):
        print("\n     Lectura de Cuidadores")

        self.conexionContexto.CuidadorRepo.leerCuidador()


    def actualizarCuidador(self):
        print("\n        Actualizacion Cuidador")
        rut = input("\nIngrese rut de cuidador: ")
        
        print(
                 "Dato a modificar: \n" \
        "1. Nombre\n" \
        "2. Direccion\n" \
        "3. Telefono\n" \
        "4. Email"
        )

        accionUsuario = input("\nIngrese opcion: ")
        
        if accionUsuario == "1":
            variableModificar = "nombre"
        elif accionUsuario == "2":
            variableModificar = "direccion"
        elif accionUsuario == "3":
            variableModificar = "telefono"
        elif accionUsuario == "4":
            variableModificar = "email"
        else:
            print("\nIngrese opcion valida")
            return
        
        nuevoDato = input("\nIngrese el nuevo dato: ")

        self.conexionContexto.CuidadorRepo.actualizarCuidador(rut, variableModificar, nuevoDato)

        print("\Acción realizada con éxito, buen dia.")


    def eliminarCuidador(self):
        print("\n     Eliminar Cuidador")
        rut = input("\nIngrese rut: ")

        self.conexionContexto.CuidadorRepo.eliminarCuidador(rut)

        print("\Acción realizada con éxito, buen dia.")