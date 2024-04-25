# N: 접시수, d: 초밥 가지수, k: 연속해서 먹을 수 있는 초밥 수, c: 쿠폰번호

n, d, k, c = map(int, input().split())
plate = []

for i in range(n):
    plate.append(int(input()))

max_sushi = 0
for i in range(n):
    if i < n-k:     # i가 초밥리스트 끝에 도달하지 않도록 n=10, k=4 -> i = 6,7,8,9
        tmp = set(plate[i:i+k])
    else:       # 연속된 구간이 리스트 끝 인덱스를 초과하여 시작 부분으로 돌아가는 경우
        tmp = set(plate[i:])
        tmp.update(plate[:(i+k)%n]) # ex) 리스트 크기=10, i=8, k=4이면
                            # (8+4)%10 = 2 -> 시작 부분의 0, 1 인덱스까지
    tmp.add(c)
    max_sushi = max(max_sushi, len(tmp))

print(max_sushi)