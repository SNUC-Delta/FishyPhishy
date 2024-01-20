class Levenshtein(object):
    def __init__(self):
        pass

    def levenshtein_distance(self, s, t):
        m, n = len(s), len(t)
        d = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            d[i][0] = i
        for j in range(n + 1):
            d[0][j] = j
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
        return d[m][n]
