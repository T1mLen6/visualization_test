#moximoxi

import matplotlib.pyplot as plt
import csv
import numpy as np
  
x = []
y = []

  
with open('Pouring_Data_2023-08-14 15-14-40.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(row[1])
  

fig, ax = plt.subplots()

#ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
ax.plot(x, y, linewidth=2)

#ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
plt.xlabel("X-axis (Time [s])")
plt.ylabel("Y-axis (Percentage %)")
plt.grid()
plt.show()