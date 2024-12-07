a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите операцию +, -, *, /: ")
if c == "+":
    d = a + b
    print(d)
elif c == "-":
    d = a - b
    print(d)
elif c == "*":
    d = a * b
    print(d)
elif c == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        d = a / b
        print(d)