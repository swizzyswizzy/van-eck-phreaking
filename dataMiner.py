import matplotlib.pyplot as plt
import numpy as np
from itertools import repeat

data = []
time = []
raw = []

file = open('Antena_pozioma_png6_800x600.prn', 'r')

lines = file.readlines()


# Truncating data to 20 000 000 samples (was 20 000 002)
# and excluding first info lines

lines = lines[5:-2]

print(lines[-1])
print(lines[0])


const = -float(lines[0][0:15])
print('const: ', const)

# Number of samplepoints
N = len(lines)

print('data length: ', N)

for line in lines:
    line = line.split()
    line[0] = float(line[0])
    line[1] = float(line[1])

    line[0] += const

    raw.append([line[0], line[1]])

    data.append(line[1])
    time.append(line[0])


print('first sample:\ntime:{} \nvalue: {}'.format(time[0], (data[0])))
print('last sample:\ntime:{} \nvalue: {}'.format(time[-1], (data[-1])))

# Adding padding (zeros) to make 1 second:
#padding = 80000000

#padding = [int(0)]*padding
#newData = data + padding
newData = data
print("newdata: ", len(newData))
X = np.linspace(0, time[-1], N)
print(len(X))

data = np.load('filtered.npy')

yf = np.fft.fft(data)

yf = abs(yf)

fig = plt.figure()
fig.suptitle('Fourier Transform', fontsize=12)
plt.xlabel('Frequency [MHz]', fontsize=10)

plt.plot(yf)


plt.show()

