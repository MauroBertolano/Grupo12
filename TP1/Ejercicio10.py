def mas_larga ( a , b ):
   if (len(a) > len(b)):
       return print("\"", a , "\" es la cadena mas larga")
   else:
       return print(b , ' es la cadena mas larga');

a=input("Ingrese primer cadena: ")
b=input("Ingrese segunda cadena: ")
mas_larga(a,b)
