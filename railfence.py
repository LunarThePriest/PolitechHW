key = int(input())
text = list(input())*key
result = []

def encode(text, key):
    for i in range (key-1, len(text), key):
        result.append(text[i])
    print(result)

encode(text, key)