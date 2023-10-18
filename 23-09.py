print('''Please choose a mode:
    type "a" to count the number of every letter in your text
    type "b" to create a dictionary of all words in your text''')
mode = input()
print('Now, type in your text:')

if mode == 'a':
    text = list(input().lower())
    for i in range(97, 123):
        print(chr(i) + ": " + str(text.count(chr(i))))

elif mode == 'b':
    text = sorted(list(set(input().split(' '))))
    print(text)
    for word in text:
        if len(word) > 2:
            print(word)

else:
    print ("Please choose either 'a' or 'b'")