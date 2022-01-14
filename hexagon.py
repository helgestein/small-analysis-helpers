#better version:
import itertools as it
import matplotlib.pyplot as plt
import numpy as np
x2,y2 = 1,0
x3,y3 = 0.5,np.sqrt(2)/2
p1,p2 = np.array([x2,y2]),np.array([x3,y3])
pos = np.array([p1*n1+p2*n2 for n1,n2 in it.product([-3+i for i in range(7)],repeat=2) if abs(n1+n2)<=3])
pos = np.unique(pos)
plt.scatter(pos[:,0],pos[:,1])
plt.axis('equal')
