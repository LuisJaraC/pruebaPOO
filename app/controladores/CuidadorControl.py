from app.vista.CuidadorVista import CuidadorVista
from app.modelos.Cuidador import Cuidador

class CuidadorControl:
    def __init__(self, conexionContexto):
        self.conexionContexto = conexionContexto

        # se inicializan vista para acceder a sus metodos
        self.cuidadorVista = CuidadorVista()
        

    def ejecutar(self):
        print("dentro de ejecutar en clase cuidador control")
        accionUsuario = self.cuidadorVista.cuidadorMenu()
        print(f'{accionUsuario} de tipo {type(accionUsuario)}')

        if accionUsuario == "1":
            self.crearCuidador()
        elif accionUsuario == "2":
            pass

    def crearCuidador(self):
        # Pedimos datos, instanciamos Cuidador para luego enviarlo al repo correspondiente
        print("\nCuidador")
        rut = input("Ingrese rut: ")
        nombre = input("Ingrese nombre: ")
        direccion = input("Ingrese direccion: ")
        telefono = input("Ingrese telefono: ")
        email = input("Ingrese email: ")

        cuidador = Cuidador(rut, nombre, direccion, telefono, email)

        # Utilizamos la conexionContexto que tiene los datos de mydb
        # 
        self.conexionContexto.CuidadorRepo.crearCuidador(cuidador)
