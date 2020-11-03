def palindromo():
    x = input('Ingrese texto: ')
    z = x[::-1]
    i = (x == z)
    return i

print (palindromo())
