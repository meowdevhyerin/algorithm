# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# n = len(matrix)


def turn_90(matrix):
    n = len(matrix)
    turned = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n - 1, -1, -1):
            turned[j][n - i - 1] = matrix[i][j]
    return turned




t = int(input())
for tc in range(1, t+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    turned_90 = turn_90(matrix)
    turned_180 = turn_90(turned_90)
    turned_270 = turn_90(turned_180)

    print(f'#{tc}')

    for x, y, z in zip(turned_90, turned_180, turned_270):
        print(f"{''.join(map(str, x))} {''.join(map(str, y))} {''.join(map(str, z))}")
