def multiplicar(a):
   x=1
   for i in range(0,len(a)):
       x = x * a[i]
   return x

a=[1,2,3,4]
print(multiplicar(a))
