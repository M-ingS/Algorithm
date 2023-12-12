a = []
for i in range(7):
    n = int(input())
    a.append(n)
s = 0
k = []
for i in a:
    if i % 2 == 1:
        k.append(i)
        s = s + i
if len(k) == 0:
    print('-1')
else:
    print(s)
    print(min(k))