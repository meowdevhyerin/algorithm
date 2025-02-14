test = [
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 2]
]




def finding_start(matrix):
    for j in range(10):
        if matrix[-1][j] == 2:
            start = j
    return start

def finding_road(matrix):
    start = finding_start(matrix)
    left = -1
    right = 1
    for i in range(10 - 1, -1, -1):
        if matrix[i][start + left] == 1 and start + left > 0:
            start += left
        elif matrix[i][start + right] == 1 and start + right < 9:
            start += right
        if i == 0:
            end = start
    return end

print(finding_road(test))


