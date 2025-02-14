# 정곤이의 단조 증가하는 수


def finding_num(arr, n):
    my_list = []
    for i in range(n - 1):
        target = arr[i] * arr[i + 1]
        my_list.append(target)
    for num in my_list:
        k = str(num)
        len_k = len(k)
        if num <= 9:
            my_list.remove(num)
        for j in range(len_k - 1):
            if k[j] > k[j+1]:
                my_list.remove(num)
    return max(my_list)

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    result = finding_num(numbers, n)
    print(f'#{tc} {result}')