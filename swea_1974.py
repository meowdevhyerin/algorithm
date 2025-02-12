def find_result_in_c(matrix):
    check_matrix_c = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            check_matrix_c[i][matrix[i][j] - 1] += 1
    return check_matrix_c

def find_result_in_r(martrix):
    check_matrix_r = [[0] * 9 for _ in range(9)]
    for j in range(9):
        for i in range(9):
            check_matrix_r[i][matrix[j][i] - 1] += 1
    return check_matrix_r

def find_result_in_cell(matrix):
    check_matrix_cell = []
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            check_row = [0] * 9
            for i in range(3):
                for j in range(3):
                    check_row[matrix[k+i][l+j] - 1] += 1
                check_matrix_cell.append(check_row)
    return check_matrix_cell

def is_available(check1, check2, check3):
    for i in range(9):
        for j in range(9):
            if check1[i][j] != 1 or check2[i][j] != 1 or check3[i][j] != 1:
                return 0
    return 1


#check_matrix = [[0] * 9 for _ in range(9)]

t = int(input())
for tc in range(1, t + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    c1 = find_result_in_c(matrix)
    c2 = find_result_in_r(matrix)
    c3 = find_result_in_cell(matrix)
    result = is_available(c1, c2, c3)
    print(f'#{tc} {result}')
