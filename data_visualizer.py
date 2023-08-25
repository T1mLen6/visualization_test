#moximoxi

import matplotlib.pyplot as plt
import csv
import numpy as np
from scripy import interpolate
 
x = []
y = []

  
with open('Pouring_Data_2023-08-14 15-14-40.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        if row[3] != 0:
            print(row)
            x.append(row[0])
            y.append(row[1])
            
        
  

fig, ax = plt.subplots()

#ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
ax.plot(x, y, label='Liquid', color ='blue')
ax.set_xticks(ax.get_xticks()[::90])
ax.set_yticks(ax.get_yticks()[::50])

#Spline
x_new = np.linspace(x[0],x[-1],100)
bspline = 

#ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
plt.xlabel("X-axis (Time [s])")
plt.ylabel("Y-axis (Percentage %)")
plt.title('Robot Real-time Pouring Data')
plt.grid(color='silver', linestyle='-', linewidth=1)
plt.legend()
plt.show()