def n():
    x = int(input('Escriba un numero: '))
    if x % 2 == 0:
        return ('Es par')
    else:
        return ('Es impar')

print(n())
