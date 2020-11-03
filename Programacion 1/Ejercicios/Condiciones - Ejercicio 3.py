print ("Ingrese primer número: ")
x = int (input())
print ("Ingrese segundo número: ")
y = int (input())
print ("Ingrese tercer número: ")
z = int (input())

if x > y and x > z:
	print ("El mayor número ingresado es: ", x)
if y > x and y > z:
	print ("El mayor número ingresado es: ", y)
if z > x and z > y:
	print ("El mayor número ingresado es: ", z)
