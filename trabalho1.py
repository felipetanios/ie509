import numpy as np
from matplotlib import pyplot as plt

plays = 200
board_size = 100
dice = 6

mobility_dict = {
        1  :38,
        4  :14,
        9  :31,
        21 :42,
        28 :84,
        36 :44,
        51 :67,
        71 :91,
        80 :100,
        98 :78,
        95 :75,
        93 :73,
        87 :24,
        64 :60,
        62 :19,
        56 :53,
        49 :11,
        48 :26,
        16 :6
}

results = np.zeros((plays, board_size), dtype = np.float64)

for i in range(len(results)):
    for j in range(len(results[i])):
        
        if i == 0:
            if j < dice:
                results[i][j] = 1/dice
        if i > 0:
            results[i][j] += sum([(1/dice)*results[i-1][j-(k+1)] for k in range(dice) if j-(k+1)>=0])

        #the jumping part
        if j+1 in mobility_dict.keys():
            results[i][(mobility_dict[j+1])-1] +=  results[i][j]
            results[i][j] = 0
    

chance_to_win = []
cumulative_chance = []
for result in results:
#     with the following line we can see numeric issues
    print(np.sum(result))
    chance_to_win.append(result[-1])
    cumulative_chance.append(sum(chance_to_win))


plt.plot(chance_to_win)
plt.show()
plt.plot(cumulative_chance)
plt.show