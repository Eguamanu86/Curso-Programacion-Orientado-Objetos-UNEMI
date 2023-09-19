class Persona:

    def __init__(self, cedula, nombre, apellido, ciudad):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad

    def __str__(self):
        return f'{self.cedula}:{self.nombre} {self.apellido}'

class Cliente(Persona):

    def __init__(self,cedula, nombre, apellido, ciudad, monto):
        Persona.__init__(self,cedula, nombre, apellido, ciudad)
        self.monto = monto
