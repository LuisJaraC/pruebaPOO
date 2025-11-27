from app.vista.MascotaVista import MascotaVista
from app.modelos.Mascota import Mascota

class MascotaControl:
    def __init__(self, conexionContexto):
        self.conexionContexto = conexionContexto

        self.mascotaVista = MascotaVista()

    def ejecutar(self):
        accionUsuario = self.mascotaVista.mascotaMenu()
        
        if accionUsuario == "1":
            self.crearMascota()
        elif accionUsuario == "2":
            self.leerMascota()
        elif accionUsuario == "3":
            self.actualizarMascota()
        elif accionUsuario == "4":
            self.eliminarMascota()
        elif accionUsuario == "5":
            pass
        else:
            print("\n Ingrese valor valido ")

    def crearMascota(self):
        print("\n    Creacion Mascto")
        nombre = input("Ingrese nombre: ")
        especie = input("Ingrese especie: ")
        raza = input("Ingrese raza: ")
        edad = input("Ingrese edad: ")
        peso = input("Ingrese peso: ")
        sexo = input("Ingrese sexo: ")
        rut_cuidador = input("Ingrese rut cuidador (debe existir): ")

        mascota = Mascota(nombre, especie, raza, edad, peso, sexo, rut_cuidador)

        self.conexionContexto.MascotaRepo.crearMascota(mascota)

        print("\Acción realizada con éxito, buen dia.")

    def leerMascota(self):
        print("\n     Lectura de Mascotas")

        self.conexionContexto.MascotaRepo.leerMascota()
    
    def actualizarMascota(self):
        print("\n        Actualizacion Mascota")
        id_mascota = input("\nIngrese id de mascota: ")
        
        print(
                 "Dato a modificar: \n" \
        "1. Nombre\n" \
        "2. Especie\n" \
        "3. Raza\n" \
        "4. Edad\n" \
        "5. Peso\n" \
        "6. Sexo\n" \
        "7. Rut Cuidador"
        )

        accionUsuario = input("\nIngrese opcion: ")
        
        if accionUsuario == "1":
            variableModificar = "nombre"
        elif accionUsuario == "2":
            variableModificar = "especie"
        elif accionUsuario == "3":
            variableModificar = "raza"
        elif accionUsuario == "4":
            variableModificar = "edad"
        elif accionUsuario == "5":
            variableModificar = "peso"
        elif accionUsuario == "6":
            variableModificar = "sexo"
        elif accionUsuario == "7":
            variableModificar = "rut_cuidador"
        else:
            print("\nIngrese opcion valida")
            return
        
        nuevoDato = input("\nIngrese el nuevo dato: ")

        self.conexionContexto.MascotaRepo.actualizarMascota(id_mascota, variableModificar, nuevoDato)

        print("\Acción realizada con éxito, buen dia.")
    
    def eliminarMascota(self):
        print("\n     Eliminar Mascota")
        id_mascota = input("\nIngrese id mascota: ")

        self.conexionContexto.MascotaRepo.eliminarMascota(id_mascota)

        print("\Acción realizada con éxito, buen dia.")