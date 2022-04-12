def computeLPSArray(pat, m, next):
    # j: next배열의 인덱스 / i: 패턴의 인덱스 / m: 패턴의 전체길이
    j = 0
    i = 1
    next[0] = 0
    while i < m:
        if pat[j] == pat[i]:
            next[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                j = next[j - 1]  # 앞 글자의 탐색을 건너 뛰기
            else:
                next[i] = 0
                i += 1


def KMP(pat, txt):
    N = len(txt)
    M = len(pat)
    next = [0] * M
    computeLPSArray(pat, M, next)
    i, j = 0, 0
    while i < N-M+1:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = next[j-1]
            else:
                i += 1
        if j == M:
            print(i-j)
            j = next[j-1]
