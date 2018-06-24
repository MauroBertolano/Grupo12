# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dni = Column(Integer, nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)

class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)

    def alta(self,socio):
            self.session.add(socio)
            self.session.commit()
            return socio


    def baja(self,id_socio):
            self.session.query(Socio).filter(Socio.id == id_socio).delete()
            self.session.commit()
            return True

    def modificacion(self,socio):
            self.session.query(Socio).filter(Socio.id == socio.id).update({"nombre":socio.nombre,"dni":socio.dni,"apellido":socio.apellido})
            self.session.commit()
            return socio

    def buscar(self,id_socio):
            soc = self.session.query(Socio).filter(Socio.id == id_socio).first()
            return soc

    def buscar_todos(self):
        todos = self.session.query(Socio).all()
        return todos

    def buscar_dni(self,dni_socio):
            soc = self.session.query(Socio).filter(Socio.dni == dni_socio).first()
            return soc

    def borrar_todos(self):
            self.session.query(Socio).delete()
            self.session.commit()

def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    assert socio.id > 0


    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    assert datos.buscar_dni(socio_2.dni) == socio_2


    # modificacion
    socio.nombre = 'Moria'
    socio.apellido = 'Casan'
    socio.dni = 13264587
    datos.modificacion(socio)
    socio_modificado = datos.buscar(socio.id)
    assert socio_modificado.id == socio.id
    assert socio_modificado.nombre == 'Moria'
    assert socio_modificado.apellido == 'Casan'
    assert socio_modificado.dni == 13264587

    # todos
    assert len(datos.buscar_todos()) == 2

    # baja
    assert datos.baja(socio.id) == True

    # borrar todos
    datos.borrar_todos()
    assert len(datos.buscar_todos()) == 0


if __name__ == '__main__':
    pruebas()
