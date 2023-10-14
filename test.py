text = input()
wlist = [word.lower() for word in text.split()]
print(wlist)
wlist = wlist.sort()
for i in wlist:
    print(wlist[i])