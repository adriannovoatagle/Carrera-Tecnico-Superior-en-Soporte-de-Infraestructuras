def inversa():
    x = ["radar","hola","chau","oro","tarde"]
    z = ''
    r = list(())
    for i in x:
        z = i[::-1]
        if i == z:
            r.append(i)
    return r

print (inversa())
