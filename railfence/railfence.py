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
    return ' '.join([''.join(l) for l in enc])

def decode(enc, h):
    outlen = sum(len(word) for word in enc)
    out = ['' for _ in range(outlen)]
    words = enc.split(' ')
    width = h*2-3

    for depth, word in enumerate(words):
        pos = 0
        for i, c in enumerate(word):
            if i == 0:
                pos = depth
                #print('i=0: ' + str(c) + str(pos))
            else:
                if depth == 0 or depth == len(words) - 1:
                    pos += width + 1
                    #print ('edge: ' + str(c) + str(pos))
                else:
                    if i % 2 == 1:
                        pos += width - (depth*2) + 1
                        #print ('second: ' + str(c) + str(pos))
                    if i % 2 == 0:
                        pos += (depth*2)
                        #print ('first: ' + str(c) + str(pos))
            out[pos] = c
        #print ('nw: ' + str(pos))
            print(c, pos)
    
    return ''.join(out)

word1 = 'incomprehensible'
word = 'WECRUO ERDSOEERNTNE AIVDAC'
h = 3
print(decode(word, h))