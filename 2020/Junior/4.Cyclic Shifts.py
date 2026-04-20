T = input() # abcd
S = input() # abc
#특정단어가 string에 있는지 어떻게 찾죠? S in T
rotate_str = S
if S in T:
    print("yes")
else:
    #string 하나씩 다 만들어서 확인!
    a = False
    for i in range(len(S) - 1):
        # 앞에문자 뒤로이동,,!
        rotate_str = rotate_str[1:len(S)] + rotate_str[0:1]
        if rotate_str in T:
            a = True
    if a:
      print("yes")
    else:
      print("no")