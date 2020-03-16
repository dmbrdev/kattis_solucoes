casos = int(input())

ev = []
for i in range(0, casos):
    ev.append([int(x) for x in input().split(' ')])

res = []
for e in ev:
    for d in range(e[0], e[1]+1):
        if d not in res:
            res.append(d)

print(len(res))



