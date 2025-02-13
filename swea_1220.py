test = [[1, 0, 2, 0, 1, 0, 1], [0, 2, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 2, 2],
        [0, 0, 0, 0, 0, 1, 0], [0, 0, 2, 1, 0, 2, 1], [0, 0, 1, 2, 2, 0, 2]]

# 1이면 내려가야 함
# 2이면 올라가야 함
# 벽에 넘어가지 않으면서 현재 위치 기준 위 또는 아래가 0이어야 함
# 2가 i == 0에 있으면 사라짐, 1이 i == len(matrix)에 있으면 사라짐

n = len(test)

def check_out(matrix):
    for j in range(n):  # 2가 i == 0에 있으면 사라짐, 1이 i == len(matrix)에 있으면 사라짐
        if matrix[0][j] == 2:
            matrix[0][j] = 0
        if matrix[-1][j] == 1:
            matrix[-1][j] = 0
    return matrix

def magnetic(matrix):
    matrix = check_out(matrix)
    while True:
        old_matrix = [row[:] for row in matrix]  # 리스트 컴프리헨션으로 깊은 복사
        for i in range(n-1):
            for j in range(n):
                # 1 기준
                if matrix[i][j] == 1 and matrix[i + 1][j] == 0:
                    matrix[i][j] = 0
                    matrix[i+1][j] = 1

        for i in range(n - 1, 0, -1):  # 아래에서 위로 검사
            for j in range(n):
                if matrix[i][j] == 2 and matrix[i - 1][j] == 0:
                    matrix[i][j] = 0
                    matrix[i - 1][j] = 2

        if old_matrix == matrix:
            break

    return check_out(matrix)

result = magnetic(test)
for row in result:
    print(row)