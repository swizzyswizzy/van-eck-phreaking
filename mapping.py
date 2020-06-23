import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from itertools import repeat
import statistics
from numpy import interp
import multiprocessing
from valueMaping import mapValue
import os
from decimal import *

data = []
time = [1,1,1]
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

const = Decimal(-float(lines[0][0:15])) #Setting const and cutting two least non significant number
print('const: ', const)

# Number of samplepoints
N = len(lines)

print('data length: ', N)
      
for line in lines:
    line = line.split()
    line[0] = Decimal(line[0])
    line[1] = Decimal(line[1])

    line[0] += const
    
    if line[0] > 0.01428571428571428: #and line[0] > 0.01639344262295082:
        data.append(line[1])

    if line[0] > 0.03333333333333333:
        print(line[0], '------------')
        break
    #time.append(line[0])

    
print('first sample:\ntime:{} \nvalue: {}'.format(time[0], (data[0])))
print('last sample:\ntime:{} \nvalue: {}'.format(time[-1], (data[-1])))

data = np.array(data)

# Wyciągnąć z danych maksimum, minimum, medianę i średnie - kwadratową, harmoniczną itd.
# i ustawić je jako przedziały do mapowania wartości

maxData = np.max(data)
minData = np.min(data)
medianData = 0
meanSquareData = 0
meanData =  0

print('max: {}, min: {}'.format(maxData, minData))

leftSpan = minData
rightSpan = maxData

print('Mapping values from [-1, 1] to [0, 255]...')

num = 0
while True:
    filename = 'mappedValues-{}.npy'.format(num)
    
    if os.path.isfile(filename):
        print('File {} exists, moving along'.format(filename))
        num += 1
    else:
        print('File does not exist, creating new one: {}'.format(filename))
        break

file = open(filename, 'w')


##data = np.array(data)
for i in range(0, len(data)):
    try:
        data[i] = interp(data[i],[leftSpan, rightSpan], [0, 255])
    except:
        print(data[i-1])
np.save(filename, data)

##for i in range(0, len(data)):
##    file.write('{}\n'.format(interp(data[i],[leftSpan, rightSpan], [0, 255])))
##    

file.close()




