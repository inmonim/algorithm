import sys
from collections import Counter

input = sys.stdin.readline

def sol():
    from collections import Counter
    words = set()
    chars = []
    while (i := input().strip()) != "-":
        words.add(i)
    while (i := input().strip()) != "#":
        chars.append(i)
    for char in chars:
        char_dict = Counter(char)
        wd = {i: 0 for i in char}
        for word in words:
            word_dict = Counter(word)
            for k, v in word_dict.items():
                if char_dict.get(k) == None or char_dict[k] < v:
                    break
            else:
                for k in word_dict.keys():
                    wd[k] += 1
        M, m = max(wd.values()), min(wd.values())
        Mk, mk = [], []
        for k, v in wd.items():
            if v == M:
                Mk.append(k)
            if v == m:
                mk.append(k)  
        print(f"{''.join(sorted(mk))} {m} {''.join(sorted(Mk))} {M}")

sol()