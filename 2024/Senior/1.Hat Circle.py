import sys
input = sys.stdin.readline
n = int(input())
h = []
for i in range(n):
  h.append(int(input()))
  
ans = 0
for i in range(n//2):
  if h[i] == h[i + n//2]:
    ans += 2
    
print(ans)