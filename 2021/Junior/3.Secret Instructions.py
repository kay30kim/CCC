numbers = []

while True:
    n = int(input())
    if n == 99999:
        break
    else:
        numbers.append(n)
    
# 처음에 2개(처음 2개의 digits) 어떻게 더하지? -> 몇개의 숫자지? -> "exactly five digits"
dir = ""
for i in range(len(numbers)):
    first = numbers[i] // 10000
    second = (numbers[i] - (first * 10000)) // 1000
    d = numbers[i] - (first * 10000) - (second * 1000)
    if (first + second) % 2 == 0 and (first + second) !=0:
        dir = "right"
    elif (first + second) % 2 > 0:
        dir = "left"
    print(dir, d)