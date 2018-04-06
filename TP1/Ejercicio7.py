def es_palindromo(a):
    x=len(a)
    vuelta=""
    for i in range (0,len(a)):
        x=x-1
        vuelta=vuelta+a[x]
    if (a==vuelta):
        return print("Es palindromo")
    else:
        return print("no es palindromo")

es_palindromo("radarra")
