import sys

input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
  li.append(int(input()))
  
a = set(li)
b = sorted(a, reverse=True) # => O(10^5 * 5)
# b = sorted(a)
# b[-3]
# 시간초과? -> 10^5 = N

c = 0
for i in li:
  if i == b[2]:
    c += 1
    
print(b[2], c)