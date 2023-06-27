a = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 8, 8, 8]


def removedouble(l):
    l2 = []
    for i in range(len(l)):
        if l[i] not in l2:
            l2.append(l[i])
    return print(*l2)


removedouble(a)
