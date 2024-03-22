sik = input().split('-')    # ex) "12-3+5-6+2"
n = []      # '-'로 나눈 항들의 합을 저장할 리스트 -> ['12', '3+5', '6+2']

for i in sik:               # ['12', '3+5', '6+2']
    sum = 0
    p = i.split('+')        # +를 기준으로 split해서 리스트p로 반환
    for j in p:
        sum += int(j)
    n.append(sum)           # [12, 8, 8]

a = n[0]    # 첫 번째값에서 그 뒤에 오는 각 항목(덧셈으로 연결된 숫자들의 합)을 차례로 뺌
for i in range(1, len(n)):
    a -= n[i]
print(a)