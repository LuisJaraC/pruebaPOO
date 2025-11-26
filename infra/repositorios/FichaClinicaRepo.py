class FichaClinicaRepo:
    def __init__(self, mydb):
        self.mydb = mydb

    def crearFichaClinica(self, ficha):
        cursor = self.mydb.cursor()

        sql = "INSERT INTO ficha_clinica (id_mascota, diagnostico, Tratamientos, Restricciones_alertas) " \
        "VALUES (%s, %s, %s, %s)"

        val = (
            ficha.id_mascota,
            ficha.diagnostico,
            ficha.tratamientos,
            ficha.restricciones
        )

        cursor.execute(sql, val)

        self.mydb.commit()
        cursor.close()

    def leerFicha(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM ficha_clinica")
        resultados = cursor.fetchall()

        for ficha in resultados:
            print(ficha)
        
        cursor.close()
    
    def actualizarFicha(self,id_ficha, variableModificar, nuevoDato):
        cursor = self.mydb.cursor()

        sql = f"UPDATE ficha_clinica SET {variableModificar} = %s WHERE id_ficha = %s"
        val = (nuevoDato, id_ficha)
        cursor.execute(sql,val)

        self.mydb.commit()
        cursor.close()

    def eliminarFicha(self,id_ficha):
        cursor = self.mydb.cursor()
        cursor.execute(f"DELETE FROM ficha_clinica WHERE id_ficha = '{id_ficha}'")
        self.mydb.commit()
        cursor.close()
