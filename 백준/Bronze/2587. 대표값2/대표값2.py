k = []
for i in range(5):
    n = int(input())
    k.append(n)
s = 0
k.sort()
for i in k:
    s = s + i
avg = s / len(k)
mid = k[len(k) // 2]    # 몫을 int로 가져옴
print(int(avg))
print(mid)

#k = [int(input()) for i in range(5)]
#s = sum(i for i in k)
