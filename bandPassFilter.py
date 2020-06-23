import numpy as np
from PIL import Image
import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq
from valueMaping import mapValue
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import os
from numpy import interp

time = []
values = []

lines = np.load('mappedValues-full0.npy')

print(len(lines))
print(lines.shape)


def butter_highpass(cutoff, fs, order=10):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq #[0.30, 0.95]
    b, a = signal.butter(order, [0.2, 0.48], btype='bandpass', analog=False, output='ba')
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=8):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data, axis=0)
    return y

fps = 30 #było 30
signal = butter_highpass_filter(lines, 0.2, fps)

print(signal[0:20])


for i in range(0, len(signal)):
    time.append(signal[i][0])
    values.append(signal[i][1])

signal = []

for i in range(len(time)):
    signal.append([time[i], values[i]])



print(signal[0:20])

signal = np.array(signal)
print(signal[0:20])

values = []

for i in range(len(signal)):
    values.append(signal[i][1])

data = np.array(values)

#mapping



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
    #data[i] = abs(data[i])
    data[i] = interp(data[i],[leftSpan, rightSpan], [0, 255])
    
np.save(filename, data)

##for i in range(0, len(data)):
##    file.write('{}\n'.format(interp(data[i],[leftSpan, rightSpan], [0, 255])))
##    

file.close()


np.save('filtered.npy', signal)






