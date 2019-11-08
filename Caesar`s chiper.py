alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz""ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
enc = input('Input your text:')
key = 1
res = " "
b = -1
res1 = " "

for letter in enc:

    pos = alpha.find(letter)
    if letter in alpha:
        res = res + alpha[pos + key]

for i in enc.split():

    if i.isdigit():
        h = str(int(i) + int(key))
        i = enc.split()
        i[b] = h
        res1 += "".join(h)
        res1 += " "


print("Your encrypted text is:",res + res1 )
