n = int(input())
quad = []

for i in range(0,n):
    quad.append(input())

def verificando():
    res = []
    for i in range(0,n):
        r = []
        # Quandidade igual
        for l in quad:
            if l.count('B') != l.count('W'):
                return False

            if ('WWW' in l) or ('BBB' in l):
                return False
            # Novo - Invertendo tabela
            r.append(l[i])

        res.append(''.join(r))
    
    for r in res:
        if ('WWW' in r) or ('BBB' in r):
            return False

    return True


if verificando():
    print(1)
else:
    print(0)

