import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


m=Basemap(projection='mill',
          llcrnrlat=25,
          llcrnrlon = -130,
          urcrnrlat=50,
          urcrnrlon=-60,
          resolution='l')
NYClat,NYClon=40.7127,-74.0059
xpt,ypt=m(NYClon,NYClat)

xs=[]
ys=[]
xs.append(xpt)
ys.append(ypt)
m.drawcoastlines()
m.drawcountries(linewidth=2)
#m.drawcounties(color='darkred')
m.drawstates(color='b')
m.plot(xpt,ypt,'c*',markersize=15)
LAlat,LAlon=34.05,-118.25
xpt,ypt=m(LAlon,LAlat)
m.plot(xpt,ypt,'g^',markersize=15)
xs.append(xpt)
ys.append(ypt)
plt.plot(xs,ys,color='r',linewidth=3,label='Flight 98')
m.drawgreatcircle(NYClon,NYClat,LAlon,LAlat,color='c',linewidth=3,label='Arc')
plt.legend()
plt.show()
