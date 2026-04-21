import sys

input = sys.stdin.readline

N = int(input())

people = []

# concert_target = 3, curPos = 5, max_range = 1 -> 갈수있나없나?
# 15 -> concert, cur - 190, max_range 190
def get_time(target, curPos, speed, max_range): # 3, 5, 1, 1
    if abs(target - curPos) <= max_range: # 최대로 이동할수있는 거리보다 target이 가까우면
        return 0
    else :
        return (abs(target - curPos) - max_range) * speed # 예시 -> (3 - |5 - 1|) * 1 = (3 - 4) * 1 = -1
      
for _ in range(N):
  p, w, d = map(int, input().split())
  people.append((p, w, d))
  # max_pos = max(max_pos, p)
  
low, high = 0, 1000000000
while low <= high:
    mid = low + (high - low) // 2
    middle = sum(get_time(mid, people[i][0], people[i][1], people[i][2]) for i in range(N))
    middle_1low = sum(get_time(mid-1, people[i][0], people[i][1], people[i][2]) for i in range(N))
    middle_1high = sum(get_time(mid+1, people[i][0], people[i][1], people[i][2]) for i in range(N))
    # print(mid, middle, middle_1low, middle_1high)
    lowest = min(middle, middle_1low, middle_1high)
    if (lowest == middle):
      print(middle)
      break
    elif (lowest == middle_1low):
      high = mid - 1
    elif (lowest == middle_1high):
      low = mid + 1
    
'''
  *
*   *


    *
  * 
* 
low == middle_1low? -> 작은게 왼쪽 = 다음에 mid의 왼쪽으로 가야함

*
  *
    *
low == middle_1high? -> 작은게 오른쪽에 = 다음에 mid의 오른쪽으로 가야함
    
*   *
  *
low == middle
'''

    
  # position, w, d

  # 18 = pos, Dis = 20
  # 17 = pos - 1, 19 = pos + 1 => Dis = 17,  Dis 22
  
  # 기울기 -> 2개의 좌표(x값, y값) / 3개의 좌표
  
  # binary search 
  
  # 2) brinary search
  # 	+ 3개의 좌표 -> (mid - 1, mid, mid +1) : Distance -> 기울기 구하기
  # 1) distance를 구하는 함수
  
  # target = 3 arr[mid] = 5
  # 1 2 4 5 7 9 10  -> 9가 있는지 없는지 찾기 단 4번의 값만 볼수있음
  # ^   ^ |            
  # left = 0, right = len(arr) - 1, mid = 중간값
  # BinarySearch : 정렬이되어있는 배열에서 -> target이 있는지 없는지 search (항상 중간 값을 비교)
#   def binarySerach(arr, left, right, target):
#       while left <= right :
#           mid = (left + right) / 2
#           if arr[mid] > target:
#               right = mid - 1
#           else if arr[mid] < target:
#               left = mid + 1
#           else:
#               return True
      
#       return False
