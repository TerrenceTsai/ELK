from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from mpldatacursor import datacursor
#normfun常態分佈函數，mu: 均值，sigma:標準差，pdf:機率密度函數
def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
    
fig = plt.figure(figsize=(20,10))
ax = fig.gca(projection='3d')

# Plot a sin curve using the x and y axes.
for i,j,k,l,z,a in zip([20.5,35,50.01,50.3], [30,15.5,20,10.5],['darkgreen','seagreen','mediumspringgreen','paleturquoise'],["time#1","time#2","time#3","time#4"],[1,2,3,4],['-','--','-.',':']):
    x=np.linspace(-40,140,100)
    y=normfun(x,i,j)
    ax.plot(x, y, zs=z, zdir='y', label=l, lw=5,color=k,linestyle=a)

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ('r', 'g', 'b', 'k')


# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(-50, 140)
ax.set_ylim(0, 5)
ax.set_zlim(0, 0.04)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=40., azim=-35)
datacursor()
plt.show()