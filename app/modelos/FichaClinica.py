class FichaClinica: 
    def __init__(self, id_mascota, diagnostico, tratamientos, restricciones, fecha_creacion=None, id_ficha=None):
        self.id_ficha = id_ficha
        self.id_mascota = id_mascota
        self.fecha_creacion = fecha_creacion
        self.diagnostico = diagnostico
        self.tratamientos = tratamientos
        self.restricciones = restricciones


