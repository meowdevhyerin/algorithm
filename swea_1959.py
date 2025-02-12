def find_max(n, m, a, b):

    if n > m:
        n, m = m, n
        a, b = b, a
    max_num = float('-inf')
    for j in range(m - n + 1):
        sum_num = 0
        for i in range(n):
            sum_num += a[i] * b[i + j]
        max_num = max(max_num, sum_num)
    return max_num

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = find_max(n, m, a, b)
    print(f'#{tc} {result}')