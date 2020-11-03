x = input('Ingrese un numero: ')
r = int()
for i in x:
      r += int(i)

if r % 2 == 0:
        print('La suma de los digitos es par')
else:
        print('La suma de los digitos es impar')
