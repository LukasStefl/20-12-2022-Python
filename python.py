import os
f = open("names.txt", "rt")


d = f.read()
w = d.split()

for x in w:
    w.count("Darth")
    w.count("Luke")
    w.count("Lea")

print(w.count("Darth"))
print(w.count("Luke"))
print(w.count("Lea"))