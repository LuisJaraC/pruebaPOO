class VistaCentral:
    def __init__(self):
        pass

    def mostrarVistas(self):
        print(
            "\n           Bienvenido al menu principal\n" 
            "\n" 
            "¿A que archivo quieres acceder?\n" 
            "\n" 
            "1. Cuidador\n" 
            "2. Ficha Clinica\n" 
            "3. Mascota\n" 
            "4. Procedimiento\n" 
            "5. Veterinario\n" \
            "0. Ingrese 0 para cerrar el programa"

            )

        
        opcion = input("\nIngresa opcion: ")
    
        return opcion