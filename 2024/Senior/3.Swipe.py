n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
   
#a = [1 2 3 4 5]
#L 5 4
#b = [1 2 2 2 7]
# swipe로 바꿀수 있다 = 같은 값이어야 한다 => 같은 값이면 하나의 값으로 압축해서 나타내자
#a = [1 2 3 5]

# 압축(같은거 생략)(값, left, right) -> 압축한것을 a랑 비교 -> 가능한지 불가능한지?
c = []
#c.append([a[0], 0, 0]) # 어느 index에서 시작해서, 어느 index까지 갔는지?!
'''바뀌기전 코드 (같은거를 계속넣음..! idx_from값이 바뀌어야함)
for idx_from in range(0, len(b) - 1):
    add = 1
    if b[idx_from] == b[idx_from + 1]: # 안 같은거 -> 더해주기
        while  idx_from + add < len(b) and b[idx_from] == b[idx_from + add]:
            add += 1
        c.append([b[idx_from], idx_from, idx_from + add - 1])'''
idx_from = 0
idx_to = 0
while idx_to < n:
    while idx_from < n and idx_to < n and b[idx_from] == b[idx_to]:
        idx_to += 1
    c.append([b[idx_from], idx_from, idx_to - 1])
    idx_from = idx_to

left = []
right = []
j = 0
for i in range(len(a)):
    if j >= len(c):
        break
    # a랑 c의 idx를 비교
    c_val, from_idx, to_idx = c[j]
    if a[i] == c_val:
        if i > from_idx:
            # swipe left
            left.append([from_idx, i])
        if i < to_idx:
            # swipe right
            right.append([i, to_idx])
        j += 1


# 결과 출력
if j == len(c):
    print("YES")
    print(len(left) + len(right))
    for l, r in left:
        print("L", l, r)
    right.reverse()
    for l, r in right:
        print("R", l, r)
else :
    print("NO")

'''우빈님 코드
while True:
    to = 0
    if b[i] == b[i + to]:
        to += 1
    else:
        break
'''

'''
  0 1 2 3 4
 a = [1 2 3 4 5]
 b = [1 2 3 5 5]
 c = [[5, 3, 4]]
a랑 c를 비교!
cur_idx = 4
from = 3
to = 4
# L 4(3+1) 5(4+1)
  
 a = [1 2 3 4 5]
 b = [1 2 2 2 5]
 c = [[2, 1, 3]]
a랑 c를 비교!
cur_idx = 1
from = 1
to = 3
# R 2(1+1) 4(3+1)

cur_idx > from:
    # swipe left 
cur_idx < to:
    # swipe right'''


# 이중포문으로 풀수있지만, 이중 포문으로 풀면은 timeover -> O(N) 풀이 필요..!
# 이중 포문을 사용한 풀이 접근도 필요,,!
# N < 3 * 10^6
'''
for i in range(1, len(a)):
    if a[i] != b[i]:
        for j in range(i + 1, len(a)): # -> 이중포문 유발 -> 누군가 해줬다면..! -> 미리 해서 배열에 저장
            if a[i] == b[j]:
                # left shift
                '''
        				