import matplotlib.pyplot as plt

slices=[7,2,2,13]

activites=['sleeping','eating','working','playing']

cols=['r','g','b','y']

plt.pie(slices,labels=activites,colors=cols,startangle=90,shadow=True,explode=(0.1,0,0,0),autopct='%1.1f%%')

plt.title("Time Allocation")
plt.show()