import sys
input = sys.stdin.read

n, *s = input().split()     # 입력받은 첫 문자는 n, 나머지는 s리스트에 저장
for i in range(int(n)):
    s[i] = s[i][::-1]       # 역순으로 뒤집기
s = list(map(int, s))
print(*sorted(s), sep='\n')