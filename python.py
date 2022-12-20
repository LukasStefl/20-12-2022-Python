import os

passwords = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
i = 0;
f = open("chars.txt", "w")
for y in passwords:
    for x in passwords:
        f.write(passwords[i])
        f.write(x)
        f.write('diablo')
        f.write('\n')

        f.write('diablo')
        f.write(passwords[i])
        f.write(x)
        f.write('\n')

        f.write(passwords[i])
        f.write('diablo')
        f.write(x)
        f.write('\n')
    i = i + 1
f.close()

#os.remove("chars.txt")