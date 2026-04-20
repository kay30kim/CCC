import sys
input = sys.stdin.readline

R = int(input())
C = int(input())
M = int(input())

INF = 10**18

dp_prev = [INF] * C
dp_curr = [INF] * C

val = 1

# 첫 번째 행
for j in range(C):
    dp_prev[j] = val
    val += 1
    if val > M:
        val = 1

# 나머지 행
for _ in range(1, R):
    # 첫 열
    dp_curr[0] = min(dp_prev[0], dp_prev[1]) + val
    val += 1
    if val > M:
        val = 1

    # 중간 열
    for j in range(1, C - 1):
        dp_curr[j] = min(dp_prev[j - 1], dp_prev[j], dp_prev[j + 1]) + val
        val += 1
        if val > M:
            val = 1

    # 마지막 열
    dp_curr[C - 1] = min(dp_prev[C - 2], dp_prev[C - 1]) + val
    val += 1
    if val > M:
        val = 1

    dp_prev, dp_curr = dp_curr, dp_prev

print(min(dp_prev))
