s = (input("Введіть текст:"))
k = int(input("Введіть число:"))
t = "".join([x*k for x in s])
print(t)