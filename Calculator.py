print("я калькулятор")
print("Натисни 'Enter' дял продовження")
input()
a = float(input("Введи перше число:"))
b = float(input("Введи друге число:"))
c = input("Вибери операццію (+, - ,/ , *):" )
if c == "+":
    c = a+b
    print("=", c)
elif c == "-":
    c = a-b
    print("=", c)
elif c == "*":
    c = a * b
    print("=", c)
elif c == "/":
    if b == 0:
        print("Помилка")

    else:
       c = a / b
       print("=", c)

else:
    c = ("Помилка")
    print(c)


print("Продовжемо?  (так або ні)")
k = input()
if k == "так" :

    t = input('Вибирай операцію( +, -, *, /,):')
    d = float(input("Введіть третє число:"))
    if t == "+":
        t = c + d
        print("=", t)
    elif t == "-":
        t = c - d
        print("=", t)
    elif t == "*":
        t = c * d
        print("=", t)
    elif c == "/":
        if d == 0:
            print("Помилка")

        else:
            t = c / d
            print("=", t)

    else:
        print("Помилка")

else:
    print()

