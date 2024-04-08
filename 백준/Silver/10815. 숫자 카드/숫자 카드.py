n = int(input())
card = list(map(int, input().split()))
m = int(input())
other = list(map(int, input().split()))

dic = {}

for i in other: # dic에 상근이가 가진 숫자인지 판별하는 m개 정수 모두 0으로 초기화
    dic[i] = 0

for i in card:
    if i in dic:
        dic[i] = 1

for i in dic:
    print(dic[i], end=' ')