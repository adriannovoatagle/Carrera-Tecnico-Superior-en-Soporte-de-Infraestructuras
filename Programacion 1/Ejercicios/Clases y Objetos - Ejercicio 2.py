class RaE:

    def __init__(self,x):

        self.x = x
        
    def funcion(self):
    
        U={"":"0","I":"1","II":"2","III":"3","IV":"4","V":"5","VI":"6","VII":"7","VIII":"8","IX":"9"}
        D={"":"0","X":"10","XX":"20","XXX":"30","XL":"40","L":"50","LX":"60","LXX":"70","LXXX":"80","XC":"90"} 
        C={"":"0","C":"100","CC":"200","CCC":"300","CD":"400","D":"500","DC":"600","DCC":"700","DCCC":"800","CM":"900"}

        r = int()
    
        for i in self.x:
            for c in C:
                if i == c:
                    r += int(C[i])
            for d in D:
                if i == d:
                    r += int(D[i])
            for u in U: 
                if i == u:
                    r += int(U[i])
        print('El numero decimal es:',r)

      
x1 = RaE(input('Ingrese numero romano: '))
x1.funcion()
