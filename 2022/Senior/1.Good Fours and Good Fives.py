ans = 0
N = int(input())
for b in range(N):
    remainder = N - (5 * b)
    if remainder < 0:
       break
    if remainder % 4 == 0: # a= 10
       ans += 1
print(ans)