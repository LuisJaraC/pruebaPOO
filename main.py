from infra.Conection import Conection
from app.controladores.ControladorCentral import ControladorCentral
from infra.repositorios.RepoCentral import RepoCentral

def validar_login(mydb):
    cursor = mydb.cursor()
    intentos = 0
    
    print("\n=== SISTEMA DE SEGURIDAD VETERINARIA ===")
    
    while intentos < 3:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        
        # Consulta directa simple (sin Repositorios para ahorrar tiempo)
        sql = "SELECT * FROM USUARIO WHERE nombre_usuario = %s AND contrasena = %s"
        val = (usuario, password)
        
        cursor.execute(sql, val)
        resultado = cursor.fetchone() # Busca si existe 1 registro
        
        if resultado:
            print(f"\n¡Bienvenido {usuario}!")
            cursor.close()
            return True # Login Exitoso
        else:
            print("Credenciales incorrectas.")
            intentos += 1
            print(f"Intentos restantes: {3 - intentos}\n")
    
    cursor.close()
    return False # Falló 3 veces

def main():
    conexion = Conection()
    if conexion is None:
        print("Error al conectar a la DB")
        return #detencion del programa

    #Obtenemos objeto de conexion y lo pasamos a RepoCentral en su constructor
    #Así repo central iniciliza cada repo, evitamos main sobrepoblado
    mydb = conexion.get_conection()

    # Seguridad validacion entrada
    if not validar_login(mydb):
        print("Acceso denegado. Cerrando el sistema...\n")
        return
    
    print(f"\nConexion exitosa a host: {conexion.host}")

    conexionContexto = RepoCentral(mydb)

    app = ControladorCentral(conexionContexto)
    app.ejecutar()
   


if __name__ == "__main__":
    main()
