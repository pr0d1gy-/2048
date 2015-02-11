n = [1, 2, 2, 2, 4, 4]

new_line = []
for i in n:
    if new_line:
        if new_line[-1] == i:
            new_line[-1] += i
        else:
            new_line.append(i)
    else:
        new_line.append(i)

print new_line
)