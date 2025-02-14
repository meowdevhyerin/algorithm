def sorting(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr



def make_sorted_list(arr):
    arr = sorting(arr)
    n = len(arr)
    sorted_list = [0] * n
    small = 0
    large = n - 1
    for i in range(n):
        if i % 2 == 0:
            sorted_list[i] = arr[large]
            large -= 1
        else:
            sorted_list[i] = arr[small]
            small += 1
    return sorted_list[:10]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    target = list(map(int, input().split()))
    result = make_sorted_list(target)
    print(f'#{tc}', *result)
