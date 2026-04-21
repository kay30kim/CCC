M = int(input())
N = int(input())
K = int(input())
#difficult
list = []
for i in range(K):
    list.append(input().split())

# N = 4, M = 5, K = 7
# R 3
# C 1
# C 2
# R 2
# R 2
# C 1
# R 4
# BGBBB
# BGBBB
# GBGGG
# GBGGG
# 생각의 흐름 -> N,M 10 ^ 12 -> k까지 안 겹치는 이중포문을 안 하거나 덜하는 풀이 필요..!
# R, C든 변화를 준 열이나 행만 G가 생길 가능성이 있다.
# 짝수번 변화 -> Black, 홀수번 변화 -> Gold

# 풀이
# 1) Row 배열 생성 -> Row변화 Counting (몇 번째 row가 몇 번 변하는지)
# 2) Col 배열 생성 -> Col변화 Counting (몇 번째 col이 몇 번 변하는지)
# 3) 각 좌표에서 홀수번 반복된곳 = Gold

pattern = [["" for _ in range(N)] for _ in range(M)]
row = [0 for _ in range(M)]
col = [0 for _ in range(N)]

for i in range(K):
    op = list[i][0]
    idx = int(list[i][1])
    if op == "R":
        row[idx - 1] += 1
    else:
        col[idx - 1] += 1
ans = 0
for i in range(M):
    for j in range(N):
        if (row[i] + col[j]) % 2 == 1:
            ans += 1
            
print(ans)