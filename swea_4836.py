def coloring(start_c, start_r, end_c, end_r, color):
    red_blocks = []
    blue_blocks = []
    for i in range(start_c, end_c + 1):
        for j in range(start_r, end_r + 1):
            if color == 1:
                red_blocks.append([i, j])
            else:
                blue_blocks.append([i, j])
    if color == 1:
        return red_blocks
    else:
        return blue_blocks


def find_purple_blocks(red_b, blue_b):
    count = 0
    if len(red_b) > len(blue_b):
        for blocks in blue_b:
            if blocks in red_b:
                count += 1
    else:
        for blocks in red_b:
            if blocks in blue_b:
                count += 1
    return count


# 원하는 출력이 나오려면 어떻게 해야 할지 고민하기

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    red_blocks = []
    blue_blocks = []
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1:
            red_blocks.extend(coloring(r1, c1, r2, c2, color))
        else:
            blue_blocks.extend(coloring(r1, c1, r2, c2, color))
    result = find_purple_blocks(red_blocks, blue_blocks)
    print(f'#{tc} {result}')
