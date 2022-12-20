import os

passwords = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

f = open("chars.txt", "w")
for x in passwords:
    f.write(x)
    f.write(x)
    f.write('\n')
f.close()
