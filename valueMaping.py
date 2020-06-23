from scipy.interpolate import interp1d


def dataMaping(data: list) -> list:
    #Check also with  [0,1] -> [0, 255] i [-1, 0] -> [0,255] and make sums
    for i in range(len(data)):
             #Conversion from (0, 1) -> (0, 255) pixel brightness
        data[i] = mapValue(data[i], -1, 1, 0, 255)
    return data


def mapValue(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
