import random
get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF),range(n)))
for i in range(1000):
    hoo = get_colors(4100) # sample return:  ['#8af5da', '#fbc08c', '#b741d0', '#e599f1', '#bbcb59', '#a2a6c0']
    if 4000 - len(set(hoo)) > 0:
        print(4000 - len(set(hoo)))
