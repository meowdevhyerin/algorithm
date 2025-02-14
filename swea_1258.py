graph = [
    [1, 2, 0, 0],
    [0, 0, 0, 0],
    [9, 4, 2, 0],
    [1, 7, 3, 0]
]

n = 4

# def find_matrix(matrix):
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] != 0:

#
# def dfs(i, j):
#     if i < 0 or i > n or j < 0 or j > n:
#         return False
#     if graph[i][j] != 0:
#         size_i, size_j = 1, 1


# dfs 함수 정의
def dfs(i, j, visited):
    # 경계 검사
    if i > len(graph) or i < 0 or j > len(graph) or j < 0:
        return 0, 0

    # 벽이거나, 이미 방문했는지 확인
    if graph[i][j] == 0 or (i, j) in visited:
        return 0, 0

    visited.add(i, j)

    d = ((-1, 0), (1, 0), (0, -1), (0, 1))

    ni = i + d[]





# 메인 함수 정의
def find_matrix(graph):
    n = len(graph)
    visited = set()
    count = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and (i, j) not in visited:

                pass

