import matplotlib.pyplot as plt

x=[1,2,3]
y=[5,4,7]

x2=[1,2,3]
y2=[10,14,12]

plt.plot(x,y,label='First Line')
plt.plot(x2,y2,label='Second Line')

plt.xlabel("Plot Value")
plt.ylabel("Variable")
plt.title('Graph')
plt.legend()
plt.show()