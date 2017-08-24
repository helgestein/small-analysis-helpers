#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:15:10 2017

@author: Helge S. Stein
"""
# this script is motivated by this paper:
# Statistical analysis and interpolation of compositional data in materials science.
# by Pesenson MZ, Suram SK, Gregoire JM.
# ACS Comb Sci. 2015 Feb 9;17(2):130-6. doi: 10.1021/co5001458.

#import all the nessesary things
import numpy as np
import pandas as pd
import pylab, os
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel
from sklearn import linear_model
from matplotlib import pyplot as plt
from scipy.spatial import Delaunay

os.chdir('/Users/helge/Documents/PythonScripts/Python3/PythonCompositionPlots-master')
from myternaryutility import TernaryPlot

#find interpolating points in convex hull
def is_in_hull(p, hull):
    if not isinstance(hull,Delaunay):
        hull = Delaunay(hull)
    return hull.find_simplex(p)>=0


#xy.csv is a simple 342 coordinate file
#edx.csv contains a complete ternary file from a k1 library
xy = pd.read_csv('/Users/helge/Google Drive/kriging/xy.csv')
cmp = pd.read_csv('/Users/helge/Google Drive/kriging/edx.csv')
#scale x in mm and cmd in fractions of 1
X = xy.values/1000
Y = cmp.values/100

#define subset Xsubset, Ysubset that is fed to the GPR model
#and Xfit where fitting is done

x = np.linspace(np.min(X[:,0]),np.max(X[:,0]),50)
y = np.linspace(np.min(X[:,1]),np.max(X[:,1]),50)
xv, yv = np.meshgrid(x, y)
Xfit_ = np.array([xv.flatten(),yv.flatten()])
idx=[]
for i in range(len(Xfit_.T)):
    if is_in_hull(Xfit_[:,i], X):
        idx.append(i)

Xfit = Xfit_[:,idx]

#%% Predict using gaussian process regressor
kernel = RBF([1.0])+WhiteKernel(noise_level=0.0336)
gpr = GaussianProcessRegressor(kernel=kernel)
gpr.fit(Xsubset, Ysubset)
Ygpr, Ystd = gpr.predict(Xfit.T, return_std=True)

#%% plot predictions
ax=pylab.gca()
stp = TernaryPlot(ax, ellabels=cmp.columns) 
x,y = stp.toCart(Ygpr)
plt.scatter(x,y,s=10,c=Ystd)
stp.label(fontsize=16)
plt.colorbar()
plt.show()

