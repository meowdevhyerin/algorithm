# test = [[2, 1, 1, 2, 2], [2, 2, 1, 2, 2], [2, 2, 1, 1, 2]]


di = [-1, 1, 0, 0]  # 상하좌우
dj = [0, 0, -1, 1]


def find_max_flowers(matrix):
    max_value = 0
    for i in range(n):
        for j in range(m):
            sum_value = matrix[i][j] # 자기 자신도 더해준다
            for k in range(1, sum_value + 1):  #현재 꽃가루 값을 보고, 상하좌우로 터뜨릴 풍선 수 정하기
                for l in range(4):  # 0 ~ 3만큼 반복함, 즉 di, dj를 움직여서 상하좌우 방향 정함
                    # 조건에 맞는지 (벽에 부딪히는지) 확인 후, 조건을 만족한다면 꽃가루의 수를 더해 준다
                    # 우선 다음 좌표들을 정의한다
                    ni = i + di[l] * k
                    nj = j + dj[l] * k
                    if 0 <= ni < n and 0 <= nj < m:
                        sum_value += matrix[ni][nj]
            max_value = max(sum_value, max_value)
    return max_value

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = find_max_flowers(matrix)
    print(f'#{tc} {result}')