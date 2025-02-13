# test = [5, 8, 3, 1, 5, 6, 9, 9, 2, 2, 4]
# n = 2

def flatten(arr):
    for i in range(n):
        min_val = min(arr)
        max_val = max(arr)
        max_idx = arr.index(max_val)
        min_idx = arr.index(min_val)
        arr[max_idx] -= 1
        arr[min_idx] += 1
    return max(arr) - min(arr)

# print(flatten(test))

for tc in range(1, 11):
    n = int(input())
    target = list(map(int, input().split()))
    result = flatten(target)
    print(f'#{tc} {result}')