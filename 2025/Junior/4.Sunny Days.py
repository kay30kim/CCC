import sys
input = sys.stdin.readline

n = int(input())
weathers = [input().strip() for _ in range(n)]

# C++의 hasP 체크와 동일
hasP = False
for c in weathers:
    if c == 'P':
        hasP = True
        break

# P가 하나도 없으면 → 반드시 하루는 틀렸으므로 S 하나는 제거됨
if not hasP:
    print(n - 1)
    sys.exit(0)

left = 0
rain = 0
ans = 0

for right in range(n):
    if weathers[right] == 'P':
        rain += 1

    while rain > 1:
        if weathers[left] == 'P':
            rain -= 1
        left += 1

    ans = max(ans, right - left + 1)

print(ans)
