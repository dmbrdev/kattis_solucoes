entrada = input()

a = 0
b = 0

for e in range(0, len(entrada),2 ):
    if entrada[e] == 'A':
        a = a + int(entrada[e+1])
    else:
        b = b + int(entrada[e+1])

if a > b:
    print('A')
else:
    print('B')