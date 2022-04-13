from re import M


next = [0] * 10


def InitNext(p):
    m = len(p)
    next[0] = -1
    i, j = 0, -1
    while i < m:
        next[i] = j
        while (j >= 0 and p[i] != p[j]):
            j = next[j]
    i += 1
    j += 1


def KMP(p, t, i):
    m = len(p)
    n = len(t)
    InitNext(p)
    j = 0
    while j < m and i < n:
        while (j >= 0 and t[i] != p[j]):
            j = next[j]
        i += 1
        j += 1
    if (j == m):
        return i - m
    else:
        return i
