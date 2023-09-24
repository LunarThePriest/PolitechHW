palindromes = []
for i in range(1000):
    if str(i) == str(i)[::-1]:
        palindromes.append(i)
print(palindromes)