t, n = map(int, input().split())
a = []

for i in range(t):
    a = input()
    c = []
    for i in range(n):
        if a.count(a[i]) >= 2 :
            c.append("heavy")
        else:
            c.append("light")
    #for i in range(n):
        #print(c[i])
        
    for i in range(len(c) - 1):
        if c[i] == c[i + 1]:
            print("F")
            break
        elif i + 2 == len(c):
            print("T")