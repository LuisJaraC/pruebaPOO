class CuidadorRepo:
    def __init__(self, mydb):
        self.mydb = mydb
    
    def crearCuidador(self, cuidador):
        cursor = self.mydb.cursor()
        

        sql = "INSERT INTO cuidador (rut_cuidador, nombre, direccion, telefono, email) " \
        "VALUES (%s, %s, %s, %s, %s)"

        # tupla extrae los valores de objeto cuidador que se recibe
        val = (
            cuidador.rut, 
            cuidador.nombre, 
            cuidador.direccion, 
            cuidador.telefono, 
            cuidador.email
        )
        
        # realizamos accion en BD
        cursor.execute(sql, val)

        self.mydb.commit()
        cursor.close()

    def leerCuidador(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM cuidador")
        resultados = cursor.fetchall()

        for producto in resultados:
            print(producto)
        
        cursor.close()

    def actualizarCuidador(self, rut, variableModificar, nuevoDato):
        cursor = self.mydb.cursor()

        #Evitamos errores de comillas

        sql = f"UPDATE cuidador SET {variableModificar} = %s WHERE rut_cuidador = %s"
        val = (nuevoDato, rut)

        cursor.execute(sql, val)

        self.mydb.commit()
        cursor.close()
    
    def eliminarCuidador(self, rut):
        cursor = self.mydb.cursor()

        cursor.execute(f"DELETE FROM cuidador WHERE rut_cuidador = '{rut}'")

        self.mydb.commit()
        cursor.close()
