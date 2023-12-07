a = int(input())
b = int(input())
c = int(input())
result = a * b * c
mul = [int(x) for x in str(result)]
cnt = [0] * 10  # 0 ~ 9까지 각각 숫자를 세어줄 cnt변수 생성
for i in mul:   # 120017 이라고 치면 하나씩 인덱스를 돌면서 각 숫자 카운트 증가
    cnt[i] = cnt[i] + 1
for i in cnt:
    print(i)

