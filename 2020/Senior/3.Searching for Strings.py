# 용어 정리
# permutations of N : N길이 보장 (e.g. aab aba baa)
# def DEF(depth):
# 	if depth == N:
#		print(ans)
#		return
#	for i in range(N):
#		if visited[i]:
#			visited[i] = true
#			ans[depth] = i
#			DEF(depth + 1)
#			vistied[i] = false
# substring of N : N길이 보장 X (e.g. a, b, aa, ab, ba, aab, aba, baa)
# def DEF(depth):
#	print(ans)
#	for i in range(N):
#		if visited[i]:
#			visited[i] = true
#			ans[depth] = i
#			DEF(depth + 1)
#			vistied[i] = false

from collections import Counter

needle = input()   # needle = "abcde" len(needle) = 10^5
haystack = input() # haystack = "abcaefe" len(haystack) = 10^5

ln = len(needle)   # 3
lh = len(haystack) # 5

if ln > lh:
    print(0)
    exit()

target = Counter(needle) # {a:1, b:1, c:1}
window = Counter(haystack[:ln]) # window {d:1, a:1 ,c:1}
ans = set()

BASE = 29 # 소수
MOD = 2**61 - 1 # => 소수라는게 보장 2^3 - 1 = 7, 2^5 - 1 = 31, 2^7 = 127
hashkey_num = 0

power = [1] * (ln + 1)
for i in range(1, ln + 1):
    power[i] = (power[i - 1] * BASE) % MOD

for i in range(ln): # haystack[i] = char -> int (haystack[i] - 'a')
    val = ord(haystack[i]) - ord('a')
    hashkey_num = (hashkey_num * BASE + val) % MOD

if window == target:
   ans.add(hashkey_num) 
# a b a-z(26)
# 1 2 3
# => 1 * 29^2 + 2 * 29 + 3 * 1 = 123
# b c d
# 2 3 4 = 234 => 2*10^2 + 3*10 + 4
# 
# 2 A 4 = 

left = 0
right = ln - 1

while right < lh - 1: #
    lc = haystack[left]
    rc = haystack[right + 1]
    # print(window, left, right)
    
    window[lc] -= 1
    if window[lc] == 0:
        del window[lc]
    window[rc] += 1
    
    
    # abcde
    # abc -> bcd - > cde
    # 1 * 10^2 + 2 * 10 + 3 -> 2 * 10^2 + 3 * 10 + 4
    left_val = ord(lc) - ord('a')
    right_val = ord(rc) - ord('a')
    
    hashkey_num = ( (hashkey_num - left_val * power[ln-1]) * BASE + right_val)  % MOD
    if window == target:
        ans.add(hashkey_num)
    
    left += 1
    right += 1

print(len(ans))

# input
# The first line contains N (1 ≤ |N| ≤ 200 000), the needle string.
# The second line contains H (1 ≤ |H| ≤ 200 000), the haystack string.
# 메모리 초과 => 1000B = 1MB 4*10^6 => 500M, 524MB - 1GB초과 / 시간 초과 => 10^8 = 1억 for i in range(10^8): O(10^8)
# for i in range(10^4)
#	for j in range(10^2) => 10^2 + 10^2 + 10^2 ... + 10^2 = 10^2 * 10^4 = 10^6


''' Counter개념 설명필요
word = "banana"
c = Counter(word)
print(c)

# needle = "abc"
=> "abc", "acb", "bac", "bca", "cab", "cba"
=> a:1, b:1, c:1
# haystack = "dacbe"
              ^ ^(a:1, c:1, b:1)
'''
'''
allpermutations = list(set(permutations(needle)))
ans = 0
for i in range(len(allpermutations)):
    # print(allpermutations[i])
    s = ""
    for j in range(len(allpermutations[0])):
        s += allpermutations[i][j]
    allpermutations[i] = s

for perm in allpermutations:
    if perm in haystack:
        ans += 1
        
        
# 각 haystack의 frequency를 담는 배열 생성
frequency = []
# 각 haystack의 frequency를 저장
print(ans)
'''

'''
N(needle)   - aab
H(haystack) - abacabaa
=> needle -> 모든 경우의 수
aab aba baa


sliding window 

1 2 3 4 5 6
    ^-----^

sum = 7, idx = 0, 5 / 1, 4 / 

2+6 = 8 > 7

#) Needle 길이만큼 범위를 정해서 Haystack에서 움직이나?

'''

    