x = list((input('Ingrese número: ')))

def suma(x):
    rs = 0
    for i in x:
        rs += int(i)
    return rs

def mul(x):
    rm = 1
    for i in x:
        rm *= int(i)
    return rm

print ('La suma de todos los números ingresados es:',suma(x))
print ('La multiplicación de todos los números ingresados es:',mul(x))

