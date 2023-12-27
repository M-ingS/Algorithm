n = int(input())
su = []
for _ in range(n):
    a = int(input())
    su.append(a)
stack = []
result = []     # +,- 결과를 담을 리스트
current = 1     # 스택에 push할 현재 숫자

for k in su:
    while current <= k:    # 현재 숫자를 수열의 숫자까지 push
        stack.append(current)
        result.append('+')  # 결과리스트에 '+' 추가
        current += 1
    if stack[-1] == k:  #스택의 top이 수열의 숫자와 같으면 pop
        stack.pop()
        result.append('-')
    else:   #스택의 top이 수열의 숫자와 다르면 주어진 수열을 만들 수 없음
        print('NO')
        break
else:  # 모든 수열을 만드는데 성공했다면 결과 출력
    for i in result:
        print(i)