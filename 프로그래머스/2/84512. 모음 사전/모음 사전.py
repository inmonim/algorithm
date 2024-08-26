def solution(word):
    word_set = "AEIOU"
    word_dict = []

    def comb(i, w):
        for c in word_set:
            wc = w + c
            word_dict.append(wc)
            if i < 4:
                comb(i+1, wc)

    for c in word_set:
        word_dict.append(c)
        comb(1, c)

    word_dict.sort()

    word_dict = [i.strip() for i in word_dict]

    return word_dict.index(word)+1