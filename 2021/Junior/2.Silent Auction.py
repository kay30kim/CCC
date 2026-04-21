n = int(input())
# 2번 부터는 입력을 그대로 받기보다 조건문에 맞춰서 가려서 받는게 필요..!
names = []
bids = []
for i in range(n *2):
    if i % 2 == 0:
        names.append(input())
    else:
        bids.append(int(input()))

# 다 받는 것도 좋네요ㅎㅎ
highest = 0
idx = 0 # 가장큰 것에 idx
for i in range(len(bids)): #range에 대해서 복습필요
    if bids[i] > highest:
        highest = bids[i]
        idx = i # idx update
    
        
      
        
# idx에 대한 정보가 부족 -> 정보를 담을 곳이 부족 -> 변수 추가,,!
print(names[idx])

# runtime error -> 배열 접근 문제 (idx문제)