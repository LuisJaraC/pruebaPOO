class VeterinarioRepo:
    def __init__(self, mydb):
        self.mydb = mydb
    
    def crearVeterinario(self, vet):
        cursor = self.mydb.cursor()

        sql = "INSERT INTO veterinario (rut_veterinario, nombre, especialidad, anios_experiencia, contacto) " \
        "VALUES (%s, %s, %s, %s, %s)"

        val = (
            vet.rut_veterinario,
            vet.nombre,
            vet.especialidad,
            vet.anios_experiencia,
            vet.contacto
        )

        cursor.execute(sql, val)
        self.mydb.commit()
        cursor.close()

    def leerVeterinario(self):
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * FROM veterinario")
        resultados = cursor.fetchall()

        for vet in resultados:
            print(vet)
        cursor.close()
    
    def actualizarVeterinario(self, rut, variableModificar, nuevoDato):
        cursor = self.mydb.cursor()

        sql = f"UPDATE veterinario SET {variableModificar} = %s WHERE rut_veterinario = %s"
        val = (nuevoDato, rut)

        cursor.execute(sql, val)
        self.mydb.commit()
        cursor.close()

    def eliminarVeterinario(self, rut):
        cursor = self.mydb.cursor()

        cursor.execute(f"DELETE FROM veterinario WHERE rut_veterinario = '{rut}'")

        self.mydb.commit()
        cursor.close()
