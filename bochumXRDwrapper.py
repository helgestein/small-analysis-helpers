#HTE Bochum - HTA JCAP XRD Data wrapper
#this script writes files for AgileFD based
#on how data is being generated at HTE group at RUB

import pandas as pd
import os
import random
import string
import numpy as np

folder = '/Users/helge/Documents/Uni/DatenExperimente/JCAP-DataMine/XRDProcessingJCAP/XYZ'
intensFile = 'intens.dat' # file containing csv of XRd intensities
angleFile = 'angle.dat' # file containing csv of angles of XRD
compoFile = 'EDX.txt' # file containing composition data as output by EDX script
posFile = 'pos.dat' # position file of the wafer (typically #342 grid)

os.chdir(folder)

intensity = pd.read_csv(intensFile,header=None,delimiter=',')
angle = pd.read_csv(angleFile,header=None,delimiter=',')
compo = pd.read_csv(compoFile,delimiter='\t')
pos = pd.read_csv(posFile,delimiter='\t')
f = open('initXYZ.txt', 'w') #scecify here a proper name

f.write('Description=BochumWrapper output\n')
f.write('UUID=Nummer\n')
f.write('Format_Version=1.0\n')
f.write('// Metadata\n')
f.write('M=3\n')
f.write('Elements={},{},{}\n'.format(compo.columns[0],compo.columns[1],compo.columns[2]))
f.write('N=342\n')
f.write('Deposition=X,Y\n')
f.write('Compositions=C{},C{},C{}\n'.format(compo.columns[0],compo.columns[1],compo.columns[2]))
f.write('Substrate=Al2O3\n')
f.write('Temp_Anneal_C=1000\n')
f.write('Experiment_ID=42\n')
f.write('// Deposition/Composition data\n')
#x
#y
for xy in pos.columns:
    f.write('{}='.format(xy))
    for position in pos[xy].values[:-1]:
        f.write('{:.3f},'.format(position))
    f.write('{:.3f}\n'.format(pos[xy].values[-1]))
#composition
for element in compo.columns:
    f.write('C{}='.format(element))
    for c in compo[element].values[:-1]:
        f.write('{:.3f},'.format(c))
    f.write('{:.3f}\n'.format(compo[element].values[-1]))
    #f.write('\n')

#Q
f.write('// Integrated counts data\n')
f.write('Q=')
for q in angle[0].values[:-1]:
    f.write('{},'.format(4.0784*np.sin(q/180*np.pi)))
f.write('{}\n'.format(4.0784*np.sin(1/180*np.pi*angle[0].values[-1])))

#Intenisty I
for i in range(341):
    f.write('I{}='.format(i+1))
    for j in intensity.values[:-1,i]:
        f.write('{},'.format(j))
    f.write('{}\n'.format(intensity.values[-1,i]))
    #f.write('\n')
f.close()
