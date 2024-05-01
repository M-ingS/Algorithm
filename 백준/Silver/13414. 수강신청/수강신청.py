import sys
input = sys.stdin.readline

k, l = map(int, input().split())    # k = 수강 인원, l = 대기목록 길이

dict = {}
for i in range(l):      # 수강신청이 들어온 순서대로 학번과 순서를 키, 값으로 저장
    dict[input().rstrip()] = i

# 순서(x[1])를 기준으로 오름차순 정렬
result = sorted(dict.items(), key= lambda x:x[1])   # x[0] = 키, x[1] = 값

# 수강 인원보다 신청 인원이 적을 경우
if k > len(result):
    k = len(result)

for i in range(k):
    print(result[i][0])