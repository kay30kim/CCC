# 입력
books = input()
# L, M, S개수가 몇개씩인지
L = 0
M = 0
S = 0
for i in range(len(books)):
    if books[i] == "L":
        L += 1
    elif books[i] == "M":
        M += 1
    elif books[i] == "S":
        S += 1
# 처음부터 L개수까지 L인지 비교, 중간부분 M인지 비교, 마지막에서부터 S개수까지 S인지 비교
# -> 다르면 count증가
# L = 2, M = 2, S =1
#01234
#LLMMS
count1 = 0
count2 = 0
count3 = 0
count4 = 0
idx = 0
for i in range(L):
    if books[idx] != "L":
        if books[idx] == "M":
            count3 += 1
        count1 += 1 # L이 아닌 개수
    idx += 1

for i in range(L, M+L): # 0 ~ M -1
    if books[idx] != "M":
        if books[idx] == "L":
            count4 += 1
        count2 += 1 # M이 아닌 개수
    idx += 1

print(count1 + count2 - min(count3, count4))
'''
for i in range(L: S +L):
    if books[idx] != "S":
        count3 += 1
    idx += 1
    '''
#   MLLSML
#-> LLLSMM
#-> LLLMMS
# count1 = 1
# count2 = 1
# m_inL = 1
# l_inM = 0 
# ans = count1(L이 아닌 개수) + count2(M이 아닌 개수)
#    SMLLMS
# -> LMLSMS
# -> LLMSMS
# -> LLMMSS

#   MMMLLLS => 3이어야하는데 6이나옴..!
#   3 + 3 => 6 - (L위치에 M인 개수 혹은 M위치에 L인개수를 빼줘야지!)

# 겹치는 것까지 count => 중복된게 있다.
# LLLMS
# -> 1) S는 안 건드린다 2) M은 안건드린다
# 1) 처음부터 L만큼 돌면서 L인지 확인후 -> 아니면 M이랑 바꿔주기 -> 개수만 count -> A
# 2) L부터 L+M까지 돌면서 M인지 확인후 -> 아니면 L이랑 바꿔주기 -> 개수만 count (결국 return해야하는 것은 string이 아니라 개수!) -> B
# A + B - (?)... (A + B) / 2

