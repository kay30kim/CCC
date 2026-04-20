import itertools
import math

def char_to_index(ch):
    """'A' → 0, 'B' → 1, 'C' → 2 로 변환"""
    return ord(ch) - ord('A')

def read_input_string():
    return input().strip()

def build_prefix_sums(s):
    """문자열에서 각 문자(A,B,C)의 prefix sum 배열 생성"""
    N = len(s)
    prefix = [[0] * (N + 1) for _ in range(3)]
    for i in range(3):  # A,B,C 각각
        for j, ch in enumerate(s, start=1):
            prefix[i][j] = prefix[i][j - 1] + (char_to_index(ch) == i)
    return prefix

def get_count(prefix, char_index, start, length):
    """prefix sum을 이용해 특정 구간 내의 문자 개수 계산"""
    return prefix[char_index][start + length] - prefix[char_index][start]

def solve(prefix, a, b, c, N):
    """a,b,c 순서로 문자열을 정렬하는데 필요한 최소 변경 횟수 계산"""
    total_a = prefix[a][-1]
    total_b = prefix[b][-1]
    total_ab = total_a + total_b

    answer = math.inf

    for start in range(N - total_ab + 1):
        count_a = get_count(prefix, a, start, total_ab)
        count_b = get_count(prefix, b, start, total_ab)
        count_c = get_count(prefix, c, start, total_ab)

        missing_a = total_a - count_a
        missing_b = total_b - count_b

        first_a = get_count(prefix, a, start, total_a)
        first_b = get_count(prefix, b, start, total_b)
        first_c_a = get_count(prefix, c, start, total_a)
        first_c_b = get_count(prefix, c, start, total_b)

        current = count_c + min(
            total_a - (first_a + min(missing_a, first_c_a)),
            total_b - (first_b + min(missing_b, first_c_b))
        )

        answer = min(answer, current)

    return answer

def main():
    s = read_input_string()
    N = len(s)
    prefix = build_prefix_sums(s)

    result = math.inf
    for a, b, c in itertools.permutations(range(3)):
        result = min(result, solve(prefix, a, b, c, N))

    print(result)

if __name__ == "__main__":
    main()
