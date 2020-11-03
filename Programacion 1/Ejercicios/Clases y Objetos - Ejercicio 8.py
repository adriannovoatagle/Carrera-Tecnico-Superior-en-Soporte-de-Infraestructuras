class ej8:

    def __init__(self,x):

        self.x = x

    def funcion(self):

        t = self.x
        y = t.split(' ')
        y.reverse()
        r = ''
        for i in y:
            r += i + ' ' 
        print('Salida: ' + r)
    
x1 = ej8(input('Ingrese palabras: '))
x1.funcion()

        
