import random

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

x=Persona('jose',18,'f',755,1.50)
print(x.es_mayor_edad())
x.print_data()
