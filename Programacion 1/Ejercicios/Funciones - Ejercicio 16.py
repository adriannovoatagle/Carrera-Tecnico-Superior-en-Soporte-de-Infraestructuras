x = list((7,2,6))
y = list((1,2,3))
def superp():
    for i in x:
        for z in y:
             if i == z:
                 return True
    return False
    
print(superp())
