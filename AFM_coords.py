#AFM_coords.py reads a xls sheet with x|y|ID where coordinates are in µm
#and writes then into a .pg file so that the Bruker AFM of ZGH can read it
#this script is nessesary to somewhat automate the AFM measurements for the
#fast scan
# (c) 2017 Helge S. Stein
import os
import pandas as pd
import matplotlib.pyplot as plt

#this read in the coordinates from the specified folder/file
def read_coords(folder = '/Users/helge/Documents/pyhtonskripts/test_data',
        file = 'wdm_grid_mum.xlsx'):
    os.chdir(folder)
    return pd.read_excel('wdm_grid_mum.xlsx')

#this writes the coordinate into the specified file
#according to the Bruker Format
def write_AFM_coords(frame, file = 'AFMStep.pgm', z_coord = -17793):
    f = open(file, 'w')
    f.write('Version 1.0\n')
    for j in range(len(frame)):
        f.write('\X point: {}\n'.format(frame['x'].iloc[j]))
        f.write('\Y point: {}\n'.format(frame['y'].iloc[j]))
        f.write('\Z point: {}\n'.format(z_coord))
        f.write('\Reference: 1\n')
        f.write('\Coordinate System: 0\n')
    f.close()

#this creates a figure to see the points where measurements will be made
#color code is there where
def plot_coords(frame):
    scat = plt.scatter(frame['x'],frame['y'],
        c = frame['ID'],cmap = plt.get_cmap('viridis'))
    plt.ylabel('y-coordinate [µm]')
    plt.xlabel('x-coordinate [µm]')
    plt.axes().set_aspect('equal', 'datalim')
    cbar = plt.colorbar(scat)
    cbar.set_label('Measurement #')
    plt.savefig('AFMCoords.png', dpi = 600, format = 'png')

#run this script
coordinates = read_coords()
write_AFM_coords(coordinates)
plot_coords(coordinates)
