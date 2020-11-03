class el:

    def __init__(self,x,y):

        self.x = x
        self.y = y
        
    def funcion(self):
        
        n = self.x
        o = self.y
        r = ''
        for i in n:
            for z in n:
                if int(i) + int(z) == int(o):
                    r += str(n.index(i)+1) + ', '
                    r += str(n.index(z)+1)
                    print('Entrada: numeros = ',n,', objetivo= ',o, '\nSalida: ',r) 
                    return
                    
        

x1 = el(list((10,20,30,40,50,60,70)),50)
x1.funcion()

