'''Ejercicio 5 Escribir una funcion que tome como parámetro una lista de Estudiantes,
y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values. '''

import random
import datetime

class Persona():
    nombre=''
    edad=0
    sexo=''
    peso=0
    altura=0
    dni=''
    def es_mayor_edad(self):
        if(self.edad>=18):
            return 'Es mayor de edad'
        else:
            return 'Es menor de edad'
    def print_data(self):
        return print('nombre: ',self.nombre,'\nedad: ',self.edad,'\nsexo: ',self.sexo,'\npeso: ',self.peso,'\naltura: ',self.altura)

class Estudiante(Persona):
    nombreCarrera=''
    añoIngreso=0
    cantMaterias=0
    cantMateriasAprob=0
    def avance(self):
        return (self.cantMaterias/self.cantMateriasAprob*100)
    def edad_ingreso(self):
        return (self.edad-(int(datetime.date.today().year)-self.añoIngreso))

def carreras(est):
    c=[n.nombreCarrera for n in est]
    t={}
    for m in c:
        if(m in t.keys()):
            t[m]=t[m]+1
        else:
            t[m]=1
    return t

est1=Estudiante()
est1.nombreCarrera='Sistemas'
est2=Estudiante()
est2.nombreCarrera='Derecho'
est3=Estudiante()
est3.nombreCarrera='Sistemas'

ests=[est1,est2,est3]

print(carreras(ests))
