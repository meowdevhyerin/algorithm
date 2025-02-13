test = [[1, 4, 0, 5, 4], [4, 4, 2, 5, 0], [0, 2, 0, 3, 2], [5, 1, 2, 0, 4], [5, 2, 2, 1, 2]]
n = len(test)


def counting_list(matrix):
    count_list = []
    for i in range(1, n + 1, 2):
        count_list.append(i)
    for i in range(n-2, 0, -2):
        count_list.append(i)

    return count_list
my_list = counting_list(test)
empty_matrix = [[0] * n for _ in range(n)]
for j in my_list:
    for i in my_list:
        empty_matrix[n - j][n - i] = 1

for row in empty_matrix:
    print(row)


# def farming(matrix):
#     sum = 0
#     center = (n - 1) / 2
#     count_list = counting_list(matrix)
#     for i in range(n):
#         sum += matrix[i][center]

