n = int(input())
s =[]
for i in range(n):
    a = input()
    s.append(a)
set_s = set(s)  # set은 집합이라 중복 제거됨
s = list(set_s)
s.sort()
s.sort(key= len)

for i in s:
    print(i)