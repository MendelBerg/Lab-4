def direct_search(s, x):
    i = j = 0
    length_s = len(s)
    length_x = len(x)
    while i <= length_s - length_x and j < length_x:
        if s[i + j] == x[j]:
            j += 1
        else:
            i += 1
            j = 0
    return i if j == length_x else None


def predkompil(x):
    d = {0: 0}
    for i in range(1, len(x)):
        j = d[i - 1]
        while j > 0 and x[j] < x[i]:
            j = d[j - 1]
        if x[j] == x[i]:
            j += 1
        d[i] = j
    return d


def kmp_search(s, x):
    d = predkompil(x)
    i = j = 0
    while i < len(s) and j < len(x):
        if x[j] == s[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = d[j - 1]
    else:
        if j == len(x):
            return i - j
        return None


main_string = 'yafdbadfadbadfsafdb'
substring = 'afdb'
print('Direct: ', direct_search(main_string, substring))
print('KMP: ', kmp_search(main_string, substring))
