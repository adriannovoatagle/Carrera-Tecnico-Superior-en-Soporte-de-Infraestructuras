def duplicado():
        o = list((str(1232)))
        x = set((o.copy()))
        if len(x) != len(o):
            return True
        else:
            return False
print(duplicado())
    




    
