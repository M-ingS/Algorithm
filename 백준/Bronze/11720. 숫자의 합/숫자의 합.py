n = int(input())
a = list(map(int, input()))
sum = 0
for i in range(0, len(a)):
    sum = sum + a[i]
print(sum)