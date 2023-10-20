#key = int(input())  --
#text = input()*key  -- for launching without pygame
result = []        # --

def encode(text, key):
    for i in range (key-1, len(text), key):
        result.append(text[i])
    return result

#encode(text, key)