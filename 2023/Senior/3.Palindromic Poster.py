n, m, r, c = map(int, input().split())
# # n = 3, m = 5, r =3, c = 5 ?
# aaaaa
# aaaaa
# aaaaa

# bbbbb
# bbbbb
# bbbbb

# sssss
# sssss
# sssss

# # n = 3, m = 5, r = 0, c = 0
# qwert
# yuiop
# asdfg

# # 이런식으로 범위의 시작과 끝부터 좁혀나가기!
# # 1) map을 N x M으로 만들어야겠다.
# # 2) map을 다 만들자..!

rotated = 0
if m == c or r == 0:
  n, m, r, c = m, n, c, r
  rotated = 1

mapp = [['a' for _ in range(m)] for _ in range(n)]

# palidrome => abcba 이거만 있는게 아니라, aaaaa이거도 palindrome이다!
# 즉, 문제를 바꿔서, "N x M 배열에 row에 r개, col에 c개 만큼 b를 채워넣어라." 

# 이중포문 사용!
for i in range(r):
  for j in range(m):
    mapp[i][j] = 'b'
    
for i in range(n):
  for j in range(c):
    mapp[i][j] = 'b'

#a = 'abcdefghijklmnhopqrstuvwxyz'
if r == 0 and c == 0:
  for i in range(n):
    for j in range(m):
      mapp[0][j] = 'c'
    mapp[i][0] = 'c'
  mapp[0][0] = 'd'
elif c == 0:
  for i in range(r, n):
    mapp[i][0] = 'c'
    
# r == 0일때도 마찬가지지만, rotate등의 방식이 있으니 일단패스

flag = 0
# ★★★ 생각의 전환 -> 중간에다가 c를 넣으려니 복잡쓰 -> 그러면 가장 위에다가 palindrome이 안 되는 곳에 c를 넣어버리자!
if r == n: # 이때 c를 넣어주는 전략! -> 아닌 것만큼 가장 상단에다가 c를 넣어주면 어떨까? 
  repeats = m - c# 얼마나 c를 넣어줘야할까? c만큼 ? c//2 만큼?
  if repeats % 2 == 1:
    if m % 2 == 0: #and c % 2 == 1:
      flag = 1
    else:
      for i in range(repeats // 2):
        mapp[0][i] = 'c'
        mapp[0][m - i - 1] = 'c'
      # 가운데 c넣어주기
      mapp[0][m //2] = 'c'
  else:
    for i in range(repeats // 2):
        mapp[0][i] = 'c'
        mapp[0][m - i - 1] = 'c'
  # for i in range(m):
  #   mapp[0][i] = 'c'

if rotated:
  mapp = list(zip(*mapp))
    
if flag :
  print("IMPOSSIBLE")
else :
  if rotated:
    for i in range(m):
      for j in range(n):
        print(mapp[i][j], end ="")
      print()
  else :
    for i in range(n):
      for j in range(m):
        print(mapp[i][j], end ="")
      print()
  
# m이랑 c랑 홀수나 짝수가 같을때 
# R = 3  4  5  6
# r_m = 1  2  2  3
# 0 1 2 3 4 5
# if (m % 2 == 0 and c % 2 == 0) or (m % 2 == 1 and c % 2 == 1):
#   row_middle = 
#   col_middle = 
#   #for문으로 c만큼 돌면서
#     #가운데에 c 넣기
#   for i in range(c):
#     mapp[]
# # c == m일때도 마찬가지지만, rotate등의 방식이 있으니 일단패스





'''
4 5 1 2
[['b', 'b', 'b', 'b'],
 ['b', 'b', 'a', 'a'],
 ['b', 'b', 'a', 'a'],
 ['b', 'b', 'a', 'a'],
 ['b', 'b', 'a', 'a']]
 
 # 문) 다음을 c만 넣어서 palindrome이 아니게 바꿔보시오.
 [['a', 'a', 'a', 'a'],
 ['a', 'a', 'a', 'a'],
 ['a', 'a', 'a', 'a'],
 ['a', 'a', 'a', 'a'],
 ['a', 'a', 'a', 'a']]
 ->
 [['d', 'c', 'c', 'c'],
 ['c', 'a', 'a', 'a'],
 ['c', 'a', 'a', 'a'],
 ['c', 'a', 'a', 'a'],
 ['c', 'a', 'a', 'a']]
 
2 2 0 0
d c
c a

5 5 1 0
b b b b b
a a a a a
a a a a a
a a a a a
a a a a a

5 5 1 0
b b b b b
d c c c c
c a a a a
c a a a a
c a a a a

5 5 2 0
b b b b b
b b b b b
d c c c c
c a a a a
c a a a a

5 5 4 0
b b b b b
b b b b b
b b b b b
b b b b b
d c c c c

5 5 1 0
b b b b b
c a a a a
c a a a a
c a a a a
c a a a a

3 5 5 0
c c c c c
b b b b b
b b b b b

4 5 4 1 -> 각각 예시를 만들어보시오
c c b c c
b b c b b
b b c b b
b b b b b

3 5 3 1
c c c c c
b b c b b
b b c b b
b b c b b
3 5 3 2 -> 각각 예시를 만들어보시오
c b c b c
b c b c b
b b b b b

3 4 3 1
b b b b
b b c b
b b b b

3 4 3 2
c b b c
b b b b
b b b b
=> 즉, M이 짝수일때는 항상 홍


'''

# 1) 우선 이중포문으로 b를 다 채워넣어줌
# 2) input의 범위를 체크하고, 현재 코드에서 오류가 날 수 있는 것을 수정해줌 - input 가장 작은값, 큰 값해보기
# 3) 