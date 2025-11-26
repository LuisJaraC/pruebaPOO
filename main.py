from infra.Conection import Conection
from app.controladores.ControladorCentral import ControladorCentral
from infra.repositorios.RepoCentral import RepoCentral

def main():
    conexion = Conection()
    if conexion is None:
        print("Error al conectar a la DB")
        return #detencion del programa
    
    print(f"\nConexion exitosa a host: {conexion.host}")

    #Obtenemos objeto de conexion y lo pasamos a RepoCentral en su constructor
    #Así repo central iniciliza cada repo, evitamos main sobrepoblado
    mydb = conexion.get_conection()
    conexionContexto = RepoCentral(mydb)

    app = ControladorCentral(conexionContexto)
    app.ejecutar()
   


if __name__ == "__main__":
    main()
