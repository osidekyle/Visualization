import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('example.txt','r') as csvfile:
    plots=csv.reader(csvfile, delimiter=',')
    for rows in plots:
        x.append(int(rows[0]))
        y.append(int(rows[1]))
plt.plot(x,y,label='Loaded')
plt.title("Loaded Data")
plt.legend()
plt.show()