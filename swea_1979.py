matrix = [[1, 0, 0, 1, 0], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 0, 1], [0, 1, 1, 1, 0]]



def finding_blank(matrix):
    n = 5
    k = 3
    result_list = []
    for i in range(n):
        count = 0
        for j in range(n):
            if matrix[i][j] == 1:
                count += 1
            else:
                if count >= k:
                    result_list.append(count)
                count = 0
        if count >= k:
            result_list.append(count)
    return result_list


print(finding_blank(matrix))