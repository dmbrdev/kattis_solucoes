lista = [int(x) for x in input().split(' ')]

def troca(a, b):
    if a > b:
        return True
    else:
        return False

esperado = [1,2,3,4,5]

def ver():
    a = []
    while True:

        for i in range(0,4):

            if troca(lista[i], lista[i+1]):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux

                a.append(lista.copy())
                #print(lista)
            if lista == esperado:
                return a

r = ver()

for i in r:    
    print(' '.join(str(x) for x in i))

    

