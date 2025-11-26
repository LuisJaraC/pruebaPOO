from infra.Conection import Conection

def main():
    conexion = Conection()
    if conexion is None:
        print("Error al conectar a la DB")
        return #detencion del programa
    
    print(f"conexion exitosa a host: {conexion.host}")
   


if __name__ == "__main__":
    main()
