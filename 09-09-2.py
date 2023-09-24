txt = input().split(' ')

result = []

for word in txt:
    result.append(word[::-1])

print(' '.join(result))