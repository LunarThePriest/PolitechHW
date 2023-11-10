key = int(input())  
text = input()*key  # -- for launching without pygame

def encode(text, key):
    result = []
    for i in range (key-1, len(text), key):
        result.append(text[i])
    result = ''.join(result)
    return result

def decode(text, key):
    result = []
    n = len(text)//key
    chunks = [text[i:i + n] for i in range(0, len(text), n)]
    for i in range(n-1):
        chunks[i] = list(chunks[i])
    print(chunks)
    #for i in range(n-1):
     #   for c in chunks:
      #      if i<len(c):
       #         result.append(c[i])

    #result = ''.join(result)
    return result

'''def decode(text, key):
    result = []
    for i in range (key-1, len(text), key):
        result.append(text[0-i])
    result = ''.join(result)
    return result'''


decode(text, key)

#print(decode(text, key))