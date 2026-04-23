R=int(input())
S=int(input())
ans = R*8+S*3-28
if ans < 0:
	print(0)
else:
	print(ans)