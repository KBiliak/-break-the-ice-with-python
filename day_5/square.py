N = 30
M = 20


def horizontal_row(sym1, sym2):
    c = []
    for i in range(N):
        if i % 5 == 0:
            c.append(sym1)
        else:
            c.append(sym2)
    c.append(sym1)
    print("".join(c))


for i in range(M):
    if i % 5 == 0:
        horizontal_row("+", "-")
    else:
        horizontal_row("|", " ")

horizontal_row("+", "-")

