# 입력받기
C = int(input())
up = list(map(int, input().split()))
down = list(map(int, input().split()))

# 1. 전체 검은색 삼각형 개수 세기 (B)
B = sum(up) + sum(down)

# 초기 테이프 길이 (3 * B)
total_tape = 3 * B

# 2. 인접한 검은색 삼각형 쌍이 있는 경우, 공유된 변만큼 테이프 길이 조정
for i in range(C):
    # 같은 행에서 인접한 검은색 삼각형
    if i < C - 1:
        if up[i] == 1 and up[i + 1] == 1:  # 위쪽 행의 인접한 삼각형
            total_tape -= 2
        if down[i] == 1 and down[i + 1] == 1:  # 아래쪽 행의 인접한 삼각형
            total_tape -= 2
    
    # 다른 행에서 인접한 검은색 삼각형 (짝수 위치에서만 발생 가능)
    if i % 2 == 0:
        if up[i] == 1 and down[i] == 1:  # 서로 다른 행에서 인접한 삼각형
            total_tape -= 2

# 최종 결과 출력
print(total_tape)
