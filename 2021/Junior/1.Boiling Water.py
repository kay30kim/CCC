n = int(input())
B = 5 * n - 400
print(B)

#determine if you are below sea level, at sea level, or above sea level.
if B > 100:
    print(-1)
elif B < 100:
    print(1)
else:
    print(0)