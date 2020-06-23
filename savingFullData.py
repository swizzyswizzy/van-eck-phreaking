import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from itertools import repeat
import statistics
from numpy import interp
from valueMaping import mapValue
import os

data = []
time = []
#screen[599][799] = 1


# File reading
file = open('stanowisko1_png5_800x600_pozioma.prn', 'r')
lines = file.readlines()
file.close()


# Truncating data
# and excluding first info lines

lines = lines[5:-2]

print(lines[-1])
print(lines[0])

const = -float(lines[0][0:15]) #Setting const and cutting two least non significant number
print('const: ', const)

# Number of samplepoints
N = len(lines)

print('data length: ', N)
      
for line in lines:
    line = line.split()
    line[0] = float(line[0])
    line[1] = float(line[1])

    line[0] += const
    
    if line[0] > 0.01666666666666666: #and line[0] > 0.01639344262295082:
        data.append([line[0], line[1]]) #[[time, value], [time value] ...]
        

    if line[0] > 0.03333333333333333:
        print(line[0], '========')
        break

    
print('first sample:\ntime:{} \nvalue: {}'.format(data[0][0], (data[0][1])))
print('last sample:\ntime:{} \nvalue: {}'.format(data[-1][0], (data[-1][1])))

data = np.array(data)

#saving to *.npy file:
num = 0
while True:
    filename = 'mappedValues-full{}.npy'.format(num)
    
    if os.path.isfile(filename):
        print('File {} exists, moving along'.format(filename))
        num += 1
    else:
        print('File does not exist, creating new one: {}'.format(filename))
        break

np.save(filename, data)
file.close()
