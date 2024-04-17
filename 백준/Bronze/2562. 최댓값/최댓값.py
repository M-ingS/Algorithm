i = 1
l =[]
while i < 10:
    i += 1
    n = int(input())
    l.append(n)

print(max(l))
print(l.index(max(l))+1)