class MiError(Exception):
    pass

def divide(x,y):
    try:
        x/y
        if (x==True or x==False or y==True or y==False):
            raise MiError('No se puede operar con True/False')
    except ZeroDivisionError:
        raise ZeroDivisionError
    except TypeError:
        raise TypeError
    else:
        return (x/y)

try:
    a=divide(6,True)
except ZeroDivisionError as e:
    print('Imposible dividir por 0; Error: ', e.args)
except TypeError as e:
    print('Tipo de dato incorrecto; Error: ', e.args)
except MiError as e:
    print('Error: ', e.args)
else:
    print('El resultado es: ', a)
