def max(a):
    max=int(a[0])
    for i in a:
        if int(i)>max:
            max=int(i)
    return max

def min(a):
    min=int(a[0])
    for i in a:
        if int(i)<min:
            min=int(i)
    return min

op=""
a=[]
while(op!="fin"):
    op=input("Ingrese numero: ")
    if (op!="fin"):
        a.append(op)
print("Maximo: ", max(a))
print("Minimo: ", min(a))
