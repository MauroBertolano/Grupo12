import random
import datetime

class Persona():
    nombre=''
    edad=0
    sexo=''
    peso=0
    altura=0
    dni=''
    def __init__(self,u,x,y,m,n):
        self.nombre=u
        self.edad=x
        self.sexo=y
        self.peso=m
        self.altura=n
        for i in range(0,7):
            self.dni=self.dni+str(random.randint(0,9))
    def es_mayor_edad(self):
        if(self.edad>=18):
            return 'Es mayor de edad'
        else:
            return 'Es menor de edad'
    def print_data(self):
        return print('nombre: ',self.nombre,'\nedad: ',self.edad,'\nsexo: ',self.sexo,'\npeso: ',self.peso,'\naltura: ',self.altura)

'''Ejercicio 4
Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
 Atributos: nombre de la carrera, año de ingreso a la misma, cantidad de materias de la
carrera, y cantidad de materias aprobadas.
 Metodos:
o avance(): indica que porcentaje de la carrera tiene aprobada.
o edad_ingreso(): indica que edad tenia al ingresar a la carrera.
'''

class Estudiante(Persona):
    nombreCarrera=''
    añoIngreso=0
    cantMaterias=0
    cantMateriasAprob=0
    def avance(self):
        return (self.cantMaterias/self.cantMateriasAprob*100)
    def edad_ingreso(self):
        return (self.edad-(int(datetime.date.today().year)-self.añoIngreso))

x=Persona('jose',18,'f',755,1.50)
print(x.es_mayor_edad())
x.print_data()
est=Estudiante('jose',18,'f',755,1.50)
est.añoIngreso=2015
print(est.edad_ingreso())
