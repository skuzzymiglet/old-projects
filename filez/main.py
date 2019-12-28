f = open("file.txt", "r")
lines = f.read()
print(lines.split("\n")[0])
f.close()
