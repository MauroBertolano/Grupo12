from TP5.Guia5 import Socio
from TP5.Guia5 import DatosSocio

class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        return self.datos.buscar_todos()

    def alta(self, socio):
        try:
            assert(self.regla_1(socio))
            assert(self.regla_2(socio))
            assert(self.regla_3())
        except DniRepetido:
            raise DniRepetido('Dni Repetido')
        except LongitudInvalida:
            raise LongitudInvalida('Longitud de nombre/apellido invalida')
        except MaximoAlcanzado:
            raise MaximoAlcanzado('Maximo de socios alcanzado')
        else:
            self.datos.alta(socio)
            return True


    def baja(self, id_socio):
        return self.datos.baja(id_socio)

    def modificacion(self, socio):
        try:
            self.regla_2(socio)
        except LongitudInvalida:
            raise LongitudInvalida
        else:
            self.datos.modificacion(socio)
            return True

    def regla_1(self, socio):
        try:
            assert(self.datos.buscar_dni(socio.dni) is None)
        except AssertionError:
            raise DniRepetido
        else:
            return True

    def regla_2(self, socio):
        try:
            assert((len(socio.nombre) >= self.MIN_CARACTERES) and (len(socio.nombre) <= self.MAX_CARACTERES) and (len(socio.apellido) >= self.MIN_CARACTERES) and (len(socio.apellido) >= self.MIN_CARACTERES))
        except AssertionError:
            raise LongitudInvalida
        else:
            return True

    def regla_3(self):
        try:
            assert(len(self.datos.buscar_todos()) != self.MAX_SOCIOS)
        except AssertionError:
            raise MaximoAlcanzado
        else:
            return True
