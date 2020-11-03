x = input('Ingrese un numero: ')
dp = ''
for i in x:
    if int(i) % 2 == 0:
        dp += i
print('Los dígitos pares del número ingresado son:',dp)
