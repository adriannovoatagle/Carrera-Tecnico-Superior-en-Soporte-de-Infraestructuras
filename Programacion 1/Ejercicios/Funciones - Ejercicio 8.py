def primo():
    r = 0
    x = int(input('Ingrese un numero: \n'))
    for i in range(1,x + 1):
        if x % i == 0:
            r += 1
    if r == 2:
        print('Es un número primo')
    else:
        print('No es un número primo')

primo()
