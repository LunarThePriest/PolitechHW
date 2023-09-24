while True:
    txt = input().split()
    a = float(txt[0])
    b = float(txt[2])

    match txt[1]:
        case "+":
            print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            if b == 0:
                print("Division by 0 is impossible.")
            else:
                print(a/b)