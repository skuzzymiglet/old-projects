x_length = int(input("X axis length = "))
y_length = int(input("Y axis length = "))
times_table = [[]]

for x in range(x_length):
    for y in range(y_length):
        times_table[x][y] = (x+1) * (y+1)


