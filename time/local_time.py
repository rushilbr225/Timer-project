import time
from numbers import zero, one, two, three, four, five, six, seven, eight, nine
import hub75
import matrixdata


from ulab import numpy





hourMap = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}


def getArrayName(i):
    return hourMap.get(i)


def combinedArray(time):
    if len(time) > 1:
        x = getArrayName(int(time[0]))
        y = getArrayName(int(time[1]))

        return numpy.concatenate((numpy.array(x, dtype=numpy.uint8), numpy.array(y, dtype=numpy.uint8)), axis=1)
    else:
        x = zero;
        y = getArrayName(int(time))
        return numpy.concatenate((numpy.array(x, dtype=numpy.uint8), numpy.array(y, dtype=numpy.uint8)), axis=1)


def fullArray(hours, minutes):
    x = combinedArray(hours)
    y = combinedArray(minutes)
    return numpy.concatenate((numpy.array(x, dtype=numpy.uint8), numpy.array(y, dtype=numpy.uint8)), axis=1)

def getTime():
    now = time.localtime()
    hours = str(now[3])
    minutes = str(now[4])
    return {1:hours,2:minutes}

# Show Python Logo
def compare(x,y):
    if(x.get(1) != y.get(1)):
        return False
    if(x.get(2) != y.get(2)):
        return False
    return True


ROW_SIZE = 16
COL_SIZE = 32

t = getTime()
x = fullArray(t.get(1), t.get(2))

config = hub75.Hub75SpiConfiguration()
matrix = matrixdata.MatrixData(ROW_SIZE, COL_SIZE)
hub75spi = hub75.Hub75Spi(matrix, config)




matrix.clear_dirty_bytes()
matrix.set_pixels(0, 0, x)

while True:    
    hub75spi.display_data()
    newTime = getTime()
    if(compare(t, newTime) == False):
        t = newTime
        x = fullArray(t.get(1), t.get(2))
        matrix.clear_dirty_bytes()
        matrix.set_pixels(0, 0, x)
    
    
