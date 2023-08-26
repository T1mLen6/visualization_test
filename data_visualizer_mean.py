#moximoxi

import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import interpolate


def tolerant_mean(arrs):
    lens = [len(i) for i in arrs]
    arr = np.ma.empty((np.max(lens),len(arrs)))
    arr.mask = True
    for idx, l in enumerate(arrs):
        arr[:len(l),idx] = l
    return arr.mean(axis = -1), arr.std(axis=-1)



x_1 = []
y_1 = []
  
with open('sorted/30/Pouring_Data_2023-08-20 19-57-22.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        #print(type(row[8]))
  
        if row[8] == 'True':
            #print(row)
            
            x_1.append(round(float(row[0]),2))
            y_1.append(float(row[2]))          
  

x_1_array = np.array(x_1) - x_1[0]
y_1_array = np.array(y_1)

x_2 = []
y_2 = []
  
with open('sorted/30/Pouring_Data_2023-08-20 19-55-27.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        #print(type(row[8]))
  
        if row[8] == 'True':
            #print(row)
            
            x_2.append(round(float(row[0]),2))
            y_2.append(float(row[2]))          
  

x_2_array = np.array(x_2) - x_2[0]
y_2_array = np.array(y_2)

y_big = [y_1_array, y_2_array]
y, error = tolerant_mean(y_big)
print(error)
fig, ax = plt.subplots()
ax.set_xlim(0,38)
ax.set_title('Robot Real-time Pouring Data (Averaged) (30%)')
ax.plot(np.arange(x_1_array[0],x_1_array[-1]+0.1, 0.1) , y, color='green')
ax.grid(color='silver', linestyle='-', linewidth=1)
ax.fill_between(np.arange(x_1_array[0],x_1_array[-1]+0.1, 0.1), y - error, y + error, color='lightgreen')
plt.show()