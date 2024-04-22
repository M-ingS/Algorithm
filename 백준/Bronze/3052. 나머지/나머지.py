l = []
for i in range(10):
    n = int(input())
    remain = n % 42

    if remain not in l:
        l.append(remain)
print(len(l))