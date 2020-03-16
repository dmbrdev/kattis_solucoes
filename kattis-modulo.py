res = []

for i in range(0,10):
    n = int(input())
    if (n % 42) not in res:
        res.append(n % 42)

print(len(res))