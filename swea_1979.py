# matrix = [[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]
n = 5
k = 3


def finding_seat(matrix):
    # 행 기준
    result = []
    for i in range(n):
        len_of_ones = 0
        for j in range(n - 1):
            if matrix[i][j] == 1 and matrix[i][j+1] == 1:
                len_of_ones += 1

        result.append(len_of_ones)

    # 열 기준
    for j in range(n):
        len_of_ones = 0
        for i in range(n - 1):
            if matrix[i][j] == 1 and matrix[i+1][j] == 1:
                len_of_ones += 1
        result.append(len_of_ones)
    count_seat = result.count(k)
    return result

matrix = [list(map(int, input().split())) for _ in range(5)]
print(finding_seat(matrix))