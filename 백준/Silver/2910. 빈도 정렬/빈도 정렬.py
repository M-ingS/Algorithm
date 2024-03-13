n, c = map(int, input().split())
num = list(map(int, input().split()))
cnt = {}        # [숫자, [등장 횟수, 처음 등장한 순서]]
k = 1           # 숫자가 등장하는 순서 기록
for i in num:
    if i in cnt:
        cnt[i][0] += 1      #[i] = 숫자, [0] = 등장횟수
    else:
        cnt[i] = [1, k]     #ex)1번 등장했으며, 처음 등장한 순서는 k번째
        k += 1

s = []
for i, j in cnt.items():
    s.append([i, j])
s.sort(key=lambda x: (-x[1][0], x[1][1]))   #x[1][0]은 해당 요소 등장횟수, x[1][1]은 해당 숫자가 처음 등장한 순서
result = []
for i, j in s:
    result += [i]*j[0]      # i를 j[0] (등장 횟수)만큼 반복 ex) i=3이고 j[0]= 2면, [3, 3]

print(*result)