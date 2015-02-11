arr = [2, 2, 4, 8]


def move_line(line):
    UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
    __size = 10
    __way = 1
    __score = 0

    n = [n for n in line if n != 0][::1 if __way in [LEFT, UP] else -1]
    if not n:
        return [0] * __size

    new_line = []
    summed = 0

    for i in n:
        if new_line and not summed:
            if new_line[-1] == i:
                new_line[-1] = i * 2
                __score += i * 2
                summed = 1
            else:
                new_line.append(i)
        else:
            new_line.append(i)
            summed = 0

    if __way in [LEFT, UP]:
        return new_line + [0] * (__size - len(new_line))

    return [0] * (__size - len(new_line)) + new_line[::-1]


print move_line(arr)