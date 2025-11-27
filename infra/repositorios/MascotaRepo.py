import mysql.connector

class MascotaRepo:
    def __init__(self, mydb):
        self.mydb = mydb

    def crearMascota(self, mascota):
        cursor = self.mydb.cursor()
        
        sql = "INSERT INTO mascota (nombre, especie, raza, edad, peso,sexo, rut_cuidador) " \
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"

        # tupla extrae los valores de objeto cuidador que se recibe
        val = (
            mascota.nombre,
            mascota.especie,
            mascota.raza,
            mascota.edad,
            mascota.peso,
            mascota.sexo,
            mascota.rut_cuidador
        )
        
        # realizamos accion en BD
        try:
            # Intentamos ejecutar la inserción
            cursor.execute(sql, val)
            self.mydb.commit()
            cursor.close()
            return True # Retornamos True si todo salió bien
            
        except mysql.connector.Error as err:
            # Capturamos si hay error
            if err.errno == 1452: #error 1452 es un error de FK
                print(f"\n[ERROR BD] El RUT de cuidador '{mascota.rut_cuidador}' no existe en la base de datos.")
            else:
                print(f"\n[ERROR BD] Ocurrió un error desconocido: {err}")
            
            cursor.close() # Cerrar cursor aunque falle
            return False # Retornamos False si falló

    
    def leerMascota(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM mascota")
        resultados = cursor.fetchall()

        for producto in resultados:
            print(producto)
        
        cursor.close()

    def actualizarMascota(self, id_mascota, variableModificar, nuevoDato):
        cursor = self.mydb.cursor()

        #Evitamos errores de comillas

        sql = f"UPDATE mascota SET {variableModificar} = %s WHERE id_mascota = %s"
        val = (nuevoDato, id_mascota)

        cursor.execute(sql, val)

        self.mydb.commit()
        cursor.close()
    
    def eliminarMascota(self, id_mascota):
        cursor = self.mydb.cursor()

        cursor.execute(f"DELETE FROM mascota WHERE id_mascota = '{id_mascota}'")

        self.mydb.commit()
        cursor.close()