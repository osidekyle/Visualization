import matplotlib.pyplot as plt
import numpy as np

x, y=np.loadtxt('example.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='Loaded with numpy')
plt.legend()
plt.show()
