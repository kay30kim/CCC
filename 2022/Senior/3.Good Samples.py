import sys
n, m, k = map(int, input().split())

ans = []
if k < n:
  print(-1)
  sys.exit()
k -= n
# 3 3 5
# 1 2 1 -> 1, 1, 1 -> 

# M 3
# ans = [1 2 3 1 2] =. 1, 2, 3, 1, 2 (1,2), (2,3) (3, 1) (1 2) (1,2,3) (2, 3, 1) (3 1 2)
# 1, 2, (1,2)
# good samples개수 1 + 2 + 3 + 3 + 3
# [1] => good samples 모두 = 1                                                              											= 총 1개
# [1,2] => good samples 모두=>1, 2, (1, 2)																																				= 총 3개 (1+ i개)
# [1,2,3] => good samples 모두=>1, 2, 3, (1,2) (2, 3) (1, 2, 3)																										= 총 6개
# [1,2,3,1] => good samples 모두=> 1, 2, 3, 1, (1, 2) (2, 3) (3, 1) (1, 2, 3) (2, 3, 1)														= 총 9개
# [1,2,3,1,2] => good samples 모두=>1, 2, 3, 1, 2, (1, 2) (2, 3) (3, 1) (1, 2) (1, 2, 3) (2, 3, 1) (3, 1 2)       = 총 12개
# 1 -> 1, 2 -> 1, 3-> 1, 4-> 1, 5 -> 1
# 1 -> 1, 2 -> 1, 3-> 1, 4-> 0

res = []
# 5 = N,  5 = M,  12 = K, res = [1, 2, 3]
for i in range(1, n + 1): # i = 5, k = 0
  k += 1												#  k = 1
  if i <= m and i <= k: 				
      k -= i										#  k = 7-2 =6-3=4-4 =1
      res.append(i)							# res = [1,2,3,4]
  elif i > m and m <= k:
      k -= m
      if i % m == 0:
      		res.append(m)
      else:
        	res.append(i % m)
  else:
      res.append(res[-k]) # res = [1,2,3,4,3] => 
      							# [1] [2] [3] [4] [3] = 5
        						# [1,2] [2,3] [3,4], [4,3] =4
                    # [1,2,3] [2,3,4]  
            				# [1,2,3,4]
      k = 0							# k = 0 
      
if k == 0:
  print(*res)
else:
  print(-1)