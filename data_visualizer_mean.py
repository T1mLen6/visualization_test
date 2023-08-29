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

def csv_opener(filename):
    x = []
    y = []
    y_foam = []
    switch = True
    index = 0
    
    y_before = 0

    with open(filename,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        
        for row in plots:
            if row[9] == 'True' and switch == True:

                align_index = index
                switch = False
    
            index += 1   
            
            if index > 1:
                x_current = round(float(row[0]),2)
                y_current = float(row[2])
                y_foam_current = float(row[3])
                
                if abs(y_current-y_before) >= 3 and x_current >= 50:
                   y_current = y_before 
                x.append(x_current)
                y.append(y_current) 
                y_foam.append(y_foam_current) 
            
                y_before = y_current
        
        offset_factor = 130 # change for every %
                
        x = x[align_index - offset_factor :]
        y = y[align_index - offset_factor :]
        y_foam = y_foam[align_index - offset_factor :]

        x_array = np.array(x) - x[0]
        y_array = np.array(y) 
        y_foam_array = np.array(y_foam) 
        
    return x_array, y_array, y_foam_array     
  
def longest(y_big):
    return max(y_big, key=len)
    
percent = 70

if percent == 30:
    x_1, y_1 = csv_opener('sorted/30/selected/Pouring_Data_2023-08-20 18-23-09.csv')
    x_2, y_2 = csv_opener('sorted/30/selected/Pouring_Data_2023-08-20 18-25-20.csv')
    x_3, y_3 = csv_opener('sorted/30/selected/Pouring_Data_2023-08-20 18-34-16.csv')
    x_4, y_4 = csv_opener('sorted/30/selected/Pouring_Data_2023-08-20 19-52-43.csv')
    x_5, y_5 = csv_opener('sorted/30/selected/Pouring_Data_2023-08-20 19-57-22.csv')    

if percent == 40:
    x_1, y_1 = csv_opener('sorted/40/selected/Pouring_Data_2023-08-20 18-12-51.csv')
    x_2, y_2 = csv_opener('sorted/40/selected/Pouring_Data_2023-08-20 18-18-30.csv')
    x_3, y_3 = csv_opener('sorted/40/selected/Pouring_Data_2023-08-20 18-20-45.csv')
    x_4, y_4 = csv_opener('sorted/40/selected/Pouring_Data_2023-08-20 19-44-23.csv')
    x_5, y_5 = csv_opener('sorted/40/selected/Pouring_Data_2023-08-20 19-47-19.csv')    

if percent == 50:
    x_1, y_1 = csv_opener('sorted/50/selected/Pouring_Data_2023-08-20 18-02-06.csv')
    x_2, y_2 = csv_opener('sorted/50/selected/Pouring_Data_2023-08-20 18-05-02.csv')
    x_3, y_3 = csv_opener('sorted/50/selected/Pouring_Data_2023-08-20 18-44-34.csv')
    x_4, y_4 = csv_opener('sorted/50/selected/Pouring_Data_2023-08-20 19-39-26.csv')
    x_5, y_5 = csv_opener('sorted/50/selected/Pouring_Data_2023-08-20 19-42-08.csv')    

if percent == 60:
    x_1, y_1 = csv_opener('sorted/60/selected/Pouring_Data_2023-08-20 17-04-54.csv')
    x_2, y_2 = csv_opener('sorted/60/selected/Pouring_Data_2023-08-20 17-07-46.csv')
    x_3, y_3 = csv_opener('sorted/60/selected/Pouring_Data_2023-08-20 17-10-46.csv')
    x_4, y_4 = csv_opener('sorted/60/selected/Pouring_Data_2023-08-20 17-13-09.csv')
    x_5, y_5 = csv_opener('sorted/60/selected/Pouring_Data_2023-08-20 17-15-28.csv')    

if percent == 70:
    x_1, y_1, y_1f = csv_opener('sorted/70/selected/Pouring_Data_2023-08-20 16-46-17.csv')
    x_2, y_2, y_2f = csv_opener('sorted/70/selected/Pouring_Data_2023-08-20 16-49-18.csv')
    x_3, y_3, y_3f = csv_opener('sorted/70/selected/Pouring_Data_2023-08-20 16-51-26.csv')
    x_4, y_4, y_4f = csv_opener('sorted/70/selected/Pouring_Data_2023-08-20 16-53-34.csv')
    x_5, y_5, y_5f = csv_opener('sorted/70/selected/Pouring_Data_2023-08-20 16-55-27.csv')    

if percent == 80:
    x_1, y_1 = csv_opener('sorted/80/selected/Pouring_Data_2023-08-20 16-34-22.csv')
    x_2, y_2 = csv_opener('sorted/80/selected/Pouring_Data_2023-08-20 16-37-22.csv')
    x_3, y_3 = csv_opener('sorted/80/selected/Pouring_Data_2023-08-20 16-39-26.csv')
    x_4, y_4 = csv_opener('sorted/80/selected/Pouring_Data_2023-08-20 16-41-28.csv')
    x_5, y_5 = csv_opener('sorted/80/selected/Pouring_Data_2023-08-20 16-44-17.csv')    
    
if percent == 90:
    x_1, y_1 = csv_opener('sorted/90/selected/Pouring_Data_2023-08-20 15-48-45.csv')
    x_2, y_2 = csv_opener('sorted/90/selected/Pouring_Data_2023-08-20 15-51-43.csv')
    x_3, y_3 = csv_opener('sorted/90/selected/Pouring_Data_2023-08-20 15-48-45.csv')
    x_4, y_4 = csv_opener('sorted/90/selected/Pouring_Data_2023-08-20 15-51-43.csv')
    x_5, y_5 = csv_opener('sorted/90/selected/Pouring_Data_2023-08-20 15-48-45.csv')    

x_big = [x_1, x_2, x_3, x_4, x_5]
y_big = [y_1, y_2, y_3, y_4, y_5]
y_bigf = [y_1f, y_2f, y_3f, y_4f, y_5f]

x_plot = longest(x_big)
y_plot, error = tolerant_mean(y_big)
y_plotf, errorf = tolerant_mean(y_bigf)

fig, ax = plt.subplots()
ax.set_xlim(0,57)# use 57 for 30%, and 38 for other percentages
ax.set_ylim(0,100)
ax.set_title('Robot Real-time Pouring Data (5-runs averaged) (' + str(percent) + '%)')

ax.grid(color='silver', linestyle='-', linewidth=1)

ax.plot(np.arange(x_plot[0],x_plot[-1]+0.1, 0.1) , y_plot, color='green', label='Liquid Mean')
ax.fill_between(np.arange(x_plot[0],x_plot[-1]+0.1, 0.1), y_plot - error, y_plot + error, color='lightgreen', label='Liquid Range', alpha = 0.6)

ax.plot(np.arange(x_plot[0],x_plot[-1]+0.1, 0.1) , y_plotf, color='crimson', label='Foam Mean')
ax.fill_between(np.arange(x_plot[0],x_plot[-1]+0.1, 0.1), y_plotf - errorf, y_plotf + errorf, color='pink', label='Foam Range', alpha = 0.6)


#ax.set_xticks([0,5,10,15,20,25,30,35,40,45,50,55]) #use this when the % = 30!!!!!!!!!!!!
ax.set_yticks(np.linspace(0, 100, num=11))
ax.set(xlabel = "Time [s]", ylabel = "Percentage %")
ax.legend()
plt.show()