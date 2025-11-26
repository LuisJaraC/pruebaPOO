class Procedimiento: 
    def __init__(self, id_ficha, rut_veterinario, tipo_procedimiento, indicaciones, costo, fecha_creacion=None, id_procedimiento=None):
        self.id_procedimiento = id_procedimiento
        self.id_ficha = id_ficha
        self.rut_veterinario = rut_veterinario
        self.fecha_creacion = fecha_creacion
        self.tipo_procedimiento = tipo_procedimiento
        self.indicaciones = indicaciones
        self.costo = costo
