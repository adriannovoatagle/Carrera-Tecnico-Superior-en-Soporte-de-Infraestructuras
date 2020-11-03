def n():
    x = int(input('Escriba un numero: '))
    y = int(input('Escriba otro numero: '))
    if x > y:
        return ('El mayor es: ' + str(x))
    else:
        return ('El mayor es: ' + str(y))

print(n())
