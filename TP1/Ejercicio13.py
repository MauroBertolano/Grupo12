m=2
band="V"
numero=int(input("Ingrese Numero: "))
while((band=="V")and (m<numero)):
   if((numero%m)==0):
       band="F"
   else:
       m=m+11
if (band=="V"):
   print("El numero es primo")
else:
   print("El numero no es primo")
