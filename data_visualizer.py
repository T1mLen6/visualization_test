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



x = []
y = []
switch = True
index = 0

  
with open('sorted/90/selected/Pouring_Data_2023-08-20 15-48-45.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        #print(type(row[8]))
  
        
        if row[9] == 'True' and switch == True:
            #print(row)
            align_index = index
            #while switch == True:
            #    [x.append(per) for per in range(index-10, index)]
            
            #x.append(round(float(row[0]),2))
            #y.append(float(row[2]))
            switch = False
        
        index += 1   
        
        if index > 1:
            x.append(round(float(row[0]),2))
            y.append(float(row[2]))   
                
        
        
                
  
print(align_index)


x = x[align_index-40 :]
y = y[align_index-40 :]

x_array = np.array(x) - x[0]
y_array = np.array(y)
fig, ax = plt.subplots(2)

#ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
ax[0].plot(x_array, y_array, label='Liquid', color ='blue')
#ax[0].set_xticks(ax.get_xticks()[::1])
#ax[0].set_yticks(ax.get_yticks()[::1])
ax[0].set_xlim(0,)

#Spline
tck = interpolate.splrep(x_array, y_array, s=0, k=3) 
x_new = np.linspace(min(x_array), max(x_array), 75)
y_fit = interpolate.BSpline(*tck)(x_new)

#x_new = np.linspace(x[0],x[-1],100)
#bspline = 
ax[1].plot(x_new, y_fit, label='Liquid', color ='red')
#ax[1].set_xticks(ax.get_xticks()[::1])
#ax[1].set_yticks(ax.get_yticks()[::1])
ax[1].set_xlim(0,)

#ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
ax[0].set(xlabel = "X-axis (Time [s])", ylabel = "Y-axis (Percentage %)")
ax[1].set(xlabel = "X-axis (Time [s])", ylabel = "Y-axis (Percentage %)")
#ax.set_ylabel("Y-axis (Percentage %)")
ax[0].set_title('Robot Real-time Pouring Data')
ax[1].set_title('Robot Real-time Pouring Data (splined)')
ax[0].grid(color='silver', linestyle='-', linewidth=1)
ax[1].grid(color='silver', linestyle='-', linewidth=1)

fig.tight_layout(h_pad=1.2)

ax[0].legend()
ax[1].legend()
plt.show()


