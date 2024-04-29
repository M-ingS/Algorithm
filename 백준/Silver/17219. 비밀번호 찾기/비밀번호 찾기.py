n, m = map(int, input().split())
dic = {}
for i in range(n):
    site, pw = input().split()
    dic[site] = pw

for _ in range(m):
    print(dic[input()])