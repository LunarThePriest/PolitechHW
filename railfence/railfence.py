def encode(word, h):
    enc = [[] for _ in range(0, h)]
    i = 0
    d = 1
    for c in word:
        enc[i].append(c)
        if i%h == h-1:
            d = -1
        if i%h == 0:
            d = 1
        i += d
    return ''.join([''.join(l) for l in enc])


def rowsplit(enc, h):
    n = len(enc) // (h+h-2)
    rem = len(enc) - n*(h + h -2)

    parts = []
    parts.append((h - 1, n + (1 if rem >= h else 0)))
    for i in range(h - 2, -1, -1):
        parts.append((i, n*(2 if i != 0 else 1) + (1 if rem >= i and rem != 0 else 0)))

    words = []
    for _, part in parts:
        words.append(enc[0: part])
        enc = enc[part:]
    return words


def decode(enc, h):
    if ' ' in enc:
        print('y')
        words = enc.split(' ')
    else:
        print('n')
        words = rowsplit(enc, h)

    outlen = sum(len(word) for word in words)
    out = ['' for _ in range(outlen)]
    width = h*2-3

    for depth, word in enumerate(words):
        pos = 0
        for i, c in enumerate(word):
            if i == 0:
                pos = depth
            else:
                if depth == 0 or depth == len(words) - 1:
                    pos += width + 1
                else:
                    if i % 2 == 1:
                        pos += width - (depth*2) + 1
                    if i % 2 == 0:
                        pos += (depth*2)
            out[pos] = c
            print(c, pos)
    
    return ''.join(out)

'''wordenc = 'incomprehensible'
wordsp = 'WECRUO ERDSOEERNTNE AIVDAC'
word = 'WECRUOERDSOEERNTNEAIVDAC'
h = 3
print(encode(wordenc, h))
print(decode(wordsp, h))
print(decode(word, h))'''