NO_OF_CHARS = 256


def bad_char_heuristic(string, size):
    bad_char = [-1] * NO_OF_CHARS
    for i in range(size):
        bad_char[ord(string[i])] = i
    return bad_char


def bm_search(txt, pat):
    m = len(pat)
    n = len(txt)
    bad_char = bad_char_heuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            print(f"Pattern occur at shift = {s}")
            s += m - bad_char[ord(txt[s + m])] if s + m < n else 1
        else:
            s += max(1, j - bad_char[ord(txt[s + j])])


txt = "ABCAAABCD"
pat = "ABC"
bm_search(txt, pat)

