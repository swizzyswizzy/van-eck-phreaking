import numpy as np
from PIL import Image
import cv2
from matplotlib import pyplot as plt
lines = np.load('mappedValues-11.npy')

print(len(lines))

parser = [0, 64, 128, 172]

lines = np.array(lines)
print(lines.shape)

#screen[100][100] = 100

height = 600 #806
width = 800 #1344

n = height*width
#n = 480000 #################################
lines = np.array_split(lines, n)

print(lines[0].shape)
print(lines[30])

for i in range(len(lines)):
    try:
        lines[i] = np.max(lines[i])
##        lines[i] = np.sort(lines[i])
##        lines[i] = lines[i][2]
        
##        for j in range(len(parser)):
##            if lines[i] <= parser[j]:
##                lines[i] = 255/(j+1)
    except:
        lines[i] = 0
        #print('EXCEPTION')
        pass

print('after processing:')
print(lines[30])

lines = np.array(lines)
print(lines.shape)
print(len(lines))


redo = True
while(redo):
    try:
        #lines = np.reshape(lines, (height, width))
        lines = np.reshape(lines, (height, width)).astype('uint8')
    except:
        np.append(lines, 0)
    else:
        redo = False


##img = Image.fromarray(lines, mode='L')
##img.show()

plt.imshow(lines, interpolation='nearest', cmap='gray_r', vmin=0, vmax=255)
plt.show()

cv2.imwrite("filename.png", lines)

print(lines[1].shape)
