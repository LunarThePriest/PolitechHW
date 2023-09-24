while True:
    txt = input().split()
    a = float(txt[0])
    b = float(txt[2])

    if txt[1] == "+":
        print(a+b)
    elif txt[1] == "-":
        print(a-b)
    elif txt[1] == "*":
        print(a*b)
    elif txt[1] == "/":
        if b == 0:
            print("Division by 0 is impossible.")
        else:
            print(a/b)