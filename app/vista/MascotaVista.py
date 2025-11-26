class MascotaVista:
    def __init__(self):
        pass

    def mascotaMenu(self):
        print(
            "\n             Menu de Mascota\n" 
            "\n" 
            "¿Que quieres hacer?\n" 
            "\n" 
            "1. Crear nuevo registro\n" 
            "2. Ver registros existentes\n" 
            "3. Actualizar datos de registros \n" 
            "4. Eliminar algun registro\n" 
            "5. Volver menu principal"
            )

        opcion = input("\nIngresa opcion: ")
        return opcion