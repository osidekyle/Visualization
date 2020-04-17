import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')

x,y,z=axes3d.get_test_data(.05)

ax1.plot_wireframe(x,y,z,rstride=3,cstride=3)

plt.show()