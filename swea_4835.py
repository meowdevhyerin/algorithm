# arr = [6262, 6004, 1801, 7660, 7919, 1280, 525, 9798, 5134, 1821]
# n = len(arr)
# m = 5

def counting_sum(nums):
    result = []
    for i in range(n - m + 1):
        sum = 0
        for j in range(m):
            sum += nums[i+j]
        result.append(sum)
    return max(result) - min(result)


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    result = counting_sum(arr)
    print(f'#{tc} {result}')