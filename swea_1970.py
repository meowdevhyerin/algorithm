money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
n = len(money_list)
# count = [0] * n
#
# money = 32850


def count_change(money):
    count = [0] * n
    for i in range(n):
        if money // money_list[i] > 0:
            count[i] = money // money_list[i]
            money -= count[i] * money_list[i]
    return count



t = int(input())
for tc in range(1, t+1):

    money = int(input())

    result = count_change(money)

    print(f'#{tc}')
    print(*result)