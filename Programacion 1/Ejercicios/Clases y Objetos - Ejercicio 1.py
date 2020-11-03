import math

class EaR:

    def __init__(self,x):

        self.x = x

    def funcion(self):
        
        U=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        D=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        C=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

        
        r = ''
        u= self.x % 10
        d=int(math.floor(self.x/10))
        c=int(math.floor(self.x/100))

        if(self.x >= 100): 
            r = C[c]+D[d]+U[u]
        elif (self.x >= 10):
            r = D[d]+U[u]
        else:
            r = U[self.x]
        print('El numero romano es:',r)
        
x1 = EaR(int(input('Ingrese un numero: ')))
x1.funcion()

