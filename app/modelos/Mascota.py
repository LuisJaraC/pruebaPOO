class Mascota: 
    def __init__(self, nombre, especie, raza, edad, peso, sexo, rut_cuidador, id_mascota=None):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.sexo = sexo
        self.rut_cuidador = rut_cuidador

