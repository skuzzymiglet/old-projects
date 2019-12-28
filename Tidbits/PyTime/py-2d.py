picture = [["a", "a", "a", "a", "a"],
           ["*", "a", "a", "a", "*"],
           ["*", "*", "a", "*", "*"],
           ["*", "a", "a", "a", "*"],
           ["a", "a", "a", "a", "a"]
    ]

for x in range(5):
    for y in range(5):
        print(picture[x][y], end="")
    print()        
