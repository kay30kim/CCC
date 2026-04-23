'''처음에 시도할때
#Definition을 그대로 구현하면 풀리는 문제
n = int(input())
heights = list(map(int, input().split()))

# |h(l+i) - h(r-i)| for 0 <= i <= (r - l) / 2 (해당 구간의 절반)
# i = 0 : |h(l) - h(r)|
# i = 1 : |h(l+1) - h(r-1)|
# i = 2 : |h(l+2) - h(r-2)|
print(heights)
ans = [999999999 for _ in range(n + 1)]
  
#1) 길이를 변화
for length in range(2, n + 1):
    for j in range(n):
        left = j
        right = length + j - 1
        if right >= n:
            break
        aVal = 0
        for i in range(0, int(((right - left) / 2) + 1)):
            if right - i >= n or left + i >= n:
                break
            aVal += abs(heights[left + i] - heights[right - i])
        ans[length] = min(ans[length], aVal)

for i in range(1, n + 1):
    if ans[i] == 999999999:
        print("0", end=" ")
    else:
	    print(ans[i], end = " ")
# 반복문 사용해서, 각 구간의 왼쪽과 오른쪽 값을 빼고 절대값을 구한다음 다 더한다
# 1) 왼쪽과 오른쪽을 결정
# 2) 반복문을 사용해서 asymmetric value 결정

# 반복문 사용해서 똑같은 것을 한 번더 해보기 (짝수/홀수)

# calculate the absolute difference in height of each of these pairs, and sum them up.
# 3 |1 4 1 5 9 2|
# aVal = 
# 길이 2 -> asymmetric value of the most symmetric picture of crops = |3 -1| = 2
# 길이 3 -> asymmetric value of the most symmetric picture of crops = 0
# 길이 4 -> asymmetric value of the most symmetric picture of crops = 5
# 길이 5 -> = 2
# 길이 6 -> = 10
# 길이 7 -> = 10
'''

n = int(input())
heights = list(map(int, input().split()))

#|h(l+i) - h(r-i)| for 0 <= i <= (r - l) / 2 (해당 구간의 절반)
#i = 0 : |h(l) - h(r)|
#i = 1 : |h(l+1) - h(r-1)|
#i = 2 : |h(l+2) - h(r-2)|
  
ans = [float('inf') for _ in range(n + 1)]

'''
7
[3 1 4 1] 5 9 2

length 4일때 asymmetric value는?
| h(l+i) - h(r-i) |
=> i = 0
1) [3 1 4 1] -> l = 0, r = 3
|3-1| + |4-1| = 5

2) [1 4 1 5] =>
|1-5| + |4-1| = 7

3) [4 1 5 9]
|4-9| + |1-5| = 9

4) [1 5 9 2]
|1-2| + |5-9| = 5
'''
min_aval_list = [[0 for _ in range(5001)] for _ in range(5001)]

#1) 길이를 변화 - sliding window
# 3 1 [4 1 5 9 2]
# for length in range(2, n + 1):
for j in range(1, n  + 1):
    left = 0
    right = j - 1 # length = right - left + 1 -> 길이도 fix
    min_aVal = 987654321
    while (right < n): # ?
        if left + 1 <= right - 1: # 홀수여서 l과 r이 같은 idx를 가리킬때
            min_aval_list[left][right] = abs(heights[left] - heights[right]) + min_aval_list[left + 1][right -1]
        else:
            min_aval_list[left][right] = abs(heights[left] - heights[right]) + 0
            # 만약 그 전까지의 최소값을 다 안다면, 현재 좌측 높이, 우측 높이의 차이랑 그 전꺼의 차이만 더하면 되지않을까?
            # 다이나믹프로그래밍
            #[1  3  4 5  6  7] left = 0, right = 5 원래대로라면 |1-7| + |3-6| + |4-5|를 다 해줘야하는데,
            # 만약, |3-6| + |4-5|가 이미 계산이 되어있다면? -> left의 index랑 right의 index만 안다면, 그 범위의 최소 aVal를 알 수있다.
            # ^  ^  ^ ^  ^  ^
        min_aVal = min(min_aVal, min_aval_list[left][right])
        left += 1
        right += 1
    print(min_aVal, end = " ")
    # for i in range(0, (right - left) / 2 + 1):
    #     aVal += heights[left + i] - heights[right - i]
    # ans[length] = min(ans[length], aVal)
