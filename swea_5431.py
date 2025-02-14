def find_bastard(test, n):
    student = list(i for i in range(1, n + 1))
    for num in test:
        if num in student:
            student.remove(num)
    return student



t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    target = list(map(int, input().split()))
    result = find_bastard(target, n)
    print(f'#{tc}', *result)