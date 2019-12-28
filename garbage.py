import random, time, sys
import matplotlib.pyplot as plt

plt.ion()

i_list = []
marks = []

for i in range(1000):
    i_list.append(i)
    
    PROBABILITY = i
    TIME = 0.5

    t1 = time.time()
    t2 = t1 + TIME

    rn = 0

    count = 0

    while True:
        if time.time() < t2:
            if random.randint(0, PROBABILITY) == 1:
                rn = random.randint(0, 9)
                count += 1
        else:
            marks.append((count/TIME)*PROBABILITY)
            print(i)
            plt.plot(i_list, marks)
            plt.show()
            break
