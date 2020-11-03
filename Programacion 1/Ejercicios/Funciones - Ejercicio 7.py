def n():
    x = int(input('Ingrese un numero: '))
    for i in range(1,x):
        x = x * i
    return ('El factorial es: ' + str(x))
    
print(n())
