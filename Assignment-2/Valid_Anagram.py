def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in s2:
        if ch in freq:
            freq[ch] -= 1
        else:
            return False

    for value in freq.values():
        if value != 0:
            return False

    return True

s1 = "salesman"
s2 = "nameless"
print(anagrams(s1, s2))
