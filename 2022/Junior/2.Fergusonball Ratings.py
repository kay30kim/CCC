num = int(input())
ans = 0
for i in range(num):
	win = int(input())
	foul = int(input())
	if (win * 5) - (foul * 3) > 40:
		ans += 1
print(ans, end="")
if ans == num:
	print("+")