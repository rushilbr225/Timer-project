import hub75
import matrixdata
from logo import logo
from time import sleep

from ulab import numpy

ROW_SIZE = 16
COL_SIZE = 32

config = hub75.Hub75SpiConfiguration()
matrix = matrixdata.MatrixData(ROW_SIZE, COL_SIZE)
hub75spi = hub75.Hub75Spi(matrix, config)

logo1 = numpy.array(logo, dtype=numpy.uint8)


# Show Python Logo

while True:    
    logo = numpy.array(logo1)
    for i in range(51):
        k = i+1
        logo1[:,i] = logo[:,k]
    logo1[:,51] = logo[:,0]    
    hub75spi.display_data()
    
    matrix.clear_dirty_bytes()
    matrix.set_pixels(0, 0, logo1)


