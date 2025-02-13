# test = [0, 0, 254, 185, 76, 227, 84, 175, 0, 0]

def counting_rooms(nums):
    count = 0
    for i in range(2, n - 2):
        if nums[i] > nums[i - 1] and nums[i] > nums[i - 2] and nums[i] > nums[i + 1] and nums[i] > nums[i + 2]:
            count += nums[i] - max(nums[i-2], nums[i+2], nums[i+1], nums[i-1])
    return count


for i in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = counting_rooms(arr)
    print(f'#{i} {result}')