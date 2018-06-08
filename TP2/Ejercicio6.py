from datetime import date
from math import floor


class Persona():

    def __init__(self,fecha_naciemiento):
        self.fecha_nacimiento = fecha_naciemiento

    def edad(self):
        return floor((date.today() - self.fecha_nacimiento).days / 365)


x = Persona(date(1997, 5, 2))
print("Edad: ", x.edad())

assert x.edad() == 21
assert x.edad() == 22
