import matplotlib.pyplot as plt
import random
from matplotlib import style

style.use('fivethirtyeight')

fig=plt.figure()

def create_plots():
    xs=[]
    ys=[]

    for i in range(10):
        x=i
        y=random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys

ax1=plt.subplot2grid((3,1),(0,0))
ax2=plt.subplot2grid((3,1),(1,0))
ax3=plt.subplot2grid((3,1),(2,0))

x,y=create_plots()
ax1.plot(x,y)

x,y=create_plots()
ax2.plot(x,y)

x,y=create_plots()
ax3.plot(x,y)

plt.show()