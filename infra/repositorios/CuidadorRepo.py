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