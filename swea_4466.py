def grade(arr, k):
    target_list = sorted(arr, reverse=True)
    sum_value = 0
    for i in range(k):
        sum_value += target_list[i]
    return sum_value


t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    target = list(map(int, input().split()))
    result = grade(target, k)
    print(f'#{tc} {result}')