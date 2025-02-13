

def find_max_sum(matrix):
    max_sum = 0
    cross_l_sum = 0
    cross_r_sum = 0
    # sum_in_cols = []
    # sum_in_rows = []
    # 가로 기준 합 탐색
    for col in matrix:
        # sum_in_cols.append(sum(col[:5]))
        max_sum = max(sum(col), max_sum)
    # 세로 기준 합 탐색
    for j in range(n):
        sum_r = 0
        for i in range(n):
            sum_r += matrix[i][j]
        max_sum = max(sum_r, max_sum)
    # 주대각선(왼쪽 위부터 오른쪽 아래까지) 기준 합 탐색
    for j in range(n):
        cross_l_sum += matrix[j][j]
        max_sum = max(cross_l_sum, max_sum)
    # 부대각선(오른쪽 위부터 왼쪽 아래까지) 기준 합 탐색
    for j in range(n):
        cross_r_sum += matrix[j][n-j-1]
        max_sum = max(cross_r_sum, max_sum)
    return max_sum

for i in range(1, 11):
    tc = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    n = 100
    result = find_max_sum(mat)
    print(f'#{tc} {result}')