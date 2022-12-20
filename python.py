import os

passwords = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

f = open("chars.txt", "w")
for y in passwords:
    for x in passwords:
        f.write(y)
        f.write(x)
        f.write('diablo')
        f.write('\n')

        f.write('diablo')
        f.write(y)
        f.write(x)
        f.write('\n')

        f.write(y)
        f.write('diablo')
        f.write(x)
        f.write('\n')


f.close()

#os.remove("chars.txt")