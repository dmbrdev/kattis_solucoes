alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = alpha.upper()

chipper = input()
key = input()
key = [x for x in key]

def buscar(a, b):
    pos_a = alpha.index(a)
    pos_b = alpha.index(b)
    return pos_a - pos_b

res = []
for i in range (0,len(chipper)):

    res.append( alpha[buscar(chipper[i], key[i])])
    
    key.append( alpha[buscar(chipper[i], key[i])])

print(''.join(res))


