print('''Please choose a mode:
    type "a" to count the number of every letter in your text
    type "b" to create a dictionary of all words in your text''')
mode = input()
print('Now, type in your text:')
text = input()

if mode == 'a':
    text = text.lower()
    for i in range(97, 123):
        temp = 0
        for symbol in text:
            if ord(symbol) == i:
                temp += 1
        print ("%s х%s"%(chr(i), temp))

elif mode == 'b':
    print(mode)
else:
    print ("Please choose either 'a' or 'b'")