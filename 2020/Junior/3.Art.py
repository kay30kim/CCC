n = int(input())
dots = []
for i in range(n):
  b = input().split(",")
  a = list(map(int, b))
  dots.append(a)
  
highest = [0, 0]
lowest = [100, 100]
# (2,2) (1,1) 이 주어지면 -> (0, 0), (3, 3)가 나와야한다
'''
2
2,2
1,1
'''
for i in range(n):
  for j in range(2):
    if dots[i][j] <= lowest[j]:
      lowest[j] = dots[i][j] - 1
    if dots[i][j] >= highest[j]:
      highest[j] = dots[i][j] + 1
      
print(str(lowest[0]) + "," + str(lowest[1]))
print(str(highest[0]) + "," + str(highest[1]))