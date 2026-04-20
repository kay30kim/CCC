import sys

def main():
    N = int(sys.stdin.readline().strip())
    burgers = list(map(int, sys.stdin.readline().split()))

    # DP[i]: i번째 사람이 방해를 당했을 때 Josh가 자기 버거를 받을 확률
    DP = [0.0] * N

    # last[type] = 이 버거 타입을 마지막으로 가진 사람의 index
    last = {}
    last[burgers[-1]] = N - 1  # Josh의 버거 타입의 마지막 사람은 Josh 자신

    totalProbability = 0.0

    # edge case: 코치와 Josh가 같은 버거 타입이면 100% 확률로 Josh가 받음
    if burgers[0] == burgers[-1]:
        print(1)
        return

    # 뒤에서부터 코치 방향으로 진행
    for i in range(N - 2, 0 - 1, -1):

        # 1) 이 사람이 코치와 같은 버거 타입
        if burgers[i] == burgers[0]:
            DP[i] = 1.0

        # 2) 같은 버거 타입의 이전 사람이 존재하면, memoization 사용
        elif burgers[i] in last:
            DP[i] = DP[last[burgers[i]]]

        # 3) 처음 등장하는 버거 타입인 경우 → 확률 계산 식 사용
        else:
            DP[i] = (1 + totalProbability) / (N - i)

        # 누적 확률 업데이트
        totalProbability += DP[i]

        # last map 갱신 (없을 때만)
        if burgers[i] not in last:
            last[burgers[i]] = i

    print(f"{totalProbability / N:.8f}")

if __name__ == "__main__":
    main()
