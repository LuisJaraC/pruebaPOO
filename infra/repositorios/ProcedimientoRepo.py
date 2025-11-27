class ProcedimientoRepo:
    def __init__(self, mydb):
        self.mydb = mydb

    def crearProcedimiento(self, procedimiento):
        cursor = self.mydb.cursor()
        #id_ficha, rut_vet, tipo, indicaciones, costo
        sql = "INSERT INTO procedimiento (id_ficha, rut_veterinario, tipo_procedimiento, indicaciones, costo) " \
        "VALUES (%s, %s, %s, %s, %s)"

        
        val = (
            procedimiento.id_ficha, 
            procedimiento.rut_veterinario, 
            procedimiento.tipo_procedimiento, 
            procedimiento.indicaciones, 
            procedimiento.costo
        )
        
        # realizamos accion en BD
        cursor.execute(sql, val)

        self.mydb.commit()
        cursor.close()

    def leerProcedimiento(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM procedimiento")
        resultados = cursor.fetchall()

        for producto in resultados:
            print(producto)
        
        cursor.close()
    
    def actualizarProcedimiento(self, id_procedimiento, variableModificar, nuevoDato):
        cursor = self.mydb.cursor()

        #Evitamos errores de comillas

        sql = f"UPDATE procedimiento SET {variableModificar} = %s WHERE id_procedimiento = %s"
        val = (nuevoDato, id_procedimiento)

        cursor.execute(sql, val)

        self.mydb.commit()
        cursor.close()

    def eliminarProcedimiento(self, id_procedimiento):
        cursor = self.mydb.cursor()

        cursor.execute(f"DELETE FROM procedimiento WHERE id_procedimiento = '{id_procedimiento}'")

        self.mydb.commit()
        cursor.close()