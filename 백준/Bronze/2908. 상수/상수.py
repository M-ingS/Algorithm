a, b = input().split()

a_r = int(a[::-1])
b_r = int(b[::-1])

print(max(a_r, b_r))
# if a_r > b_r:
#     print(a_r)
# else:
#     print(b_r)