n =  int(input())
res_final = []

for i in range(1, n+1):

    c = int(input())
    cod = input().split(' ')

    res = {}
    for j in cod:
        res[j] = cod.count(j)

    for k,v in res.items():
        if v == 1:
            res_final.append(str(f'Case #{i}: {k}'))

for f in res_final:
    print(f)