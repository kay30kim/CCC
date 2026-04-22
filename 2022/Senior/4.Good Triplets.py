import sys

def nC2(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2

def main():
    input = sys.stdin.readline
    N, C = map(int, input().split())
    P = list(map(int, input().split()))
    
    P.sort()
    
    # cnt[x] = location x에 있는 점 개수
    cnt = [0] * (C + 1)
    for x in P:
        cnt[x] += 1
    
    # 원형 확장
    P2 = P + [x + C for x in P]
    
    # 전체 조합
    ans = N * (N - 1) * (N - 2) // 6
    
    # 반원 내부에 몰린 triplet 제거
    j = 0
    half = C / 2
    for i in range(N):
        while j < 2 * N and P2[j] - P2[i] <= half:
            j += 1
        ans -= nC2(j - i - 1)
    
    # C가 짝수일 때, 정확히 C/2 정반대 위치 중복 보정
    if C % 2 == 0:
        h = C // 2
        for i in range(h):
            a = cnt[i]
            b = cnt[i + h]
            if a and b:
                ans += a * nC2(b) + nC2(a) * b
    
    print(ans)

if __name__ == "__main__":
    main()
