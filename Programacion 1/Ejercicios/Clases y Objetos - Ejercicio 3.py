class parentesis:

    def __init__(self,x):

        self.x = x
    
    def funcion(self):
                
        z = list((self.x))

        p1 = int()
        p2 = int()
        p3 = int()
        p4 = int()
        p5 = int()
        p6 = int()
        
        d = {'1':'(','2':')','3':'[','4':']','5':'{','6':'}'}
        y = list(())
        for i in z:
            if i == d['1']:
                p1 = z.count(i)
            if i == d['2']:
                p2 = z.count(i)
            if i == d['3']:
                p3 = z.count(i)
            if i == d['4']:
                p4 = z.count(i)
            if i == d['5']:
                p5 = z.count(i)
            if i == d['6']:
                p6 = z.count(i)
        
        p12 = p1

        while p12 > 0:  
            if p1 == p2:
                y.append(d['1'])
                y.append(d['2'])
            p12 -= 1
    
        p34 = p3

        while p34 > 0:
            if p3 == p4:
                y.append(d['3'])
                y.append(d['4'])
            p34 -= 1                 

        p56 = p5

        while p56 > 0:
            if p5 == p6:
                y.append(d['5'])
                y.append(d['6'])
            p56 -= 1                 

        if z == y:
            print ('La cadena ingresada es valida')
        else:
            print ('La cadena ingresada es invalida')
   
x1 = parentesis(str(input('Ingrese cadena de parentesis: ')))
x1.funcion()
