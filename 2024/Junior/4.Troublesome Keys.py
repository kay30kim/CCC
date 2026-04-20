import sys
sys.setrecursionlimit(10**6)
from collections import deque #암기!!

# 입력받고 -> 항상 습관
r = int(input())
c = int(input())

p = []

for _ in range(r):
  p.append(input())
  
rf = int(input())
cf = int(input())

ans = 0

# 확인 프린트해보기! -> 항상 습관
#print("r =", r, "c =", c)
#for i in range(r):
#  print(p[i])
#print("rf = ", rf, "cf = ", cf)

# 상하 좌우로 움직이는 flood fill함수 구현!
visited = [[0 for _ in range(c)]for _ in range(r)]
ans = 0
def flood_fill(row, col):
  if row < 0 or col < 0 or row >= r or col >= c or p[row][col] == "*" or visited[row][col] == 1:
    return
  visited[row][col] = 1
  if p[row][col] == "L":
    ans += 10
  elif p[row][col] == "M":
    ans += 5
  elif p[row][col] == "S":
    ans += 1
  flood_fill(row + 1, col)
  flood_fill(row - 1, col)
  flood_fill(row, col + 1)
  flood_fill(row, col - 1)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
  
def print0():
  for i in range(r):
    # print(p[i])
    for j in range(c):
      print(visited[i][j], end = "")
    print()
  print()
  
# r, c (처음 입력받은 좌표), // row, col (현재위치) // nr, nc (다음위치)
def dfs(depth, row, col):
  global ans
  #정답에 맞게 함수를 구현
  if p[row][col] == "L":
    ans += 10
  elif p[row][col] == "M":
    ans += 5
  elif p[row][col] == "S":
    ans += 1
#   print0()
  # 반복문
  # for i in range(N):
  # 이웃 탐색 방법 (1) 상하좌우, 대각선이든 for문으로 좌표 생성

  for k in range(4):
    nr = row + dr[k]
    nc = col + dc[k]
    # map안에 있는지 확인 -> row하면 안되고, nr
    if nr < 0 or nc < 0 or nr >= r or nc >= c:
      continue # return하면 안 됨 -> 왜?
    if visited[nr][nc] == 0 and p[nr][nc] != "*":
      visited[nr][nc] = 1
      dfs(depth + 1, nr, nc)
    #   visited[nr][nc] = 0; # 우리가 경로를 찾는것도 아닌데, 한 번 방문한 곳을 굳이? 0으로 만들 필요가있나?

def bfs(row_start, col_start):
    global ans
    # 필요한 자료구조 -> queue
    q = deque()
    # 초기값설정
    q.append([row_start, col_start])
    visited[row_start][col_start] = 1
    # 반복문 while - 조건 
    while q:
      #print0()
      row, col = q.popleft()
      if p[row][col] == "L":
        ans += 10
      elif p[row][col] == "M":
        ans += 5
      elif p[row][col] == "S":
        ans += 1
    #   print(row, col, r, c)
      # 이웃 탐개헤서 다음 좌표 설정
      for k in range(4):
        nr = row + dr[k]
        nc = col + dc[k]
        # map 안에 있는지 확인
        if nr < 0 or nc < 0 or nr >= r or nc >= c:
          continue
        if visited[nr][nc] == 0 and p[nr][nc] != "*":
          visited[nr][nc] = 1
          q.append([nr, nc])
# flood_fill(rf, cf)

# visited[rf][cf] = 1
# dfs(0, rf, cf)
bfs(rf, cf)
print(ans)










# def dfs(depth, idx, row, col):
#   # 종료조건
#   if depth < :
#     #정답에 맞게 함수를 구현
#     ans()
  
#   # 반복문
#   # for i in range(N):
#     # 이웃 탐색 방법
#   for k in range(4):
#     nr = row + dr[k]
#     nc = col + dc[k]
#     if visited[i] == 0 and ? (arr[i] == '_', arr[i] < 5):
#       visited[i] = 1;
#       arr[depth] = ?
#       dfs(depth + 1, ?)
#       visited[i] = 0;   