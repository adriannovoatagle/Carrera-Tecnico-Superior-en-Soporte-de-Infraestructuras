class ej7:

    def __init__ (self,x,n):

        self.x = x
        self.n = n

    def funcion(self):

        a = self.x
        b = self.n
        
        print('Salida: ',pow(a, b))
   


x1 = ej7(int(input('Ingrese base: ')),int(input('Ingrese exponente: ')))
x1.funcion()
