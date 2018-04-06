def superposicion(a,b):
   for n in a:
       for m in b:
           if(n==m):
               return True
   return False

lista1=['a','b','c','d','e','f','g']
lista2=['a','i','j','k','l']

print(superposicion(lista1,lista2))
