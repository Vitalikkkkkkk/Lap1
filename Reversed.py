s = input("Введіть слова:")
r = s[: :-1]
d = r.split()
st = " " .join(reversed(d))
print(st)
