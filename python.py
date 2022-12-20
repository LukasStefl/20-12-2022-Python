import os

passwords = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

f = open("demofile3.txt", "w")
for x in passwords:
    f.write(x + '\n')
f.close()
