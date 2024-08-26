import time
import hub75
import matrixdata
from ulab import numpy

# Define arrays for each letter (A to Z)
letters = {
    'A': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,1,1,1,0,0],
          [0,0,1,1,1,0,0],
          [0,1,1,0,1,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,1,1,0],
          [0,1,1,0,1,1,0],
          [0,1,1,0,1,1,0],
          [0,1,1,0,1,1,0],
          [0,1,1,0,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'B': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'C': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'D': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'E': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'F': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,1,1,0,0],
          [0,1,1,1,1,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'G': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,1,1,1,0],
          [0,0,0,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0]],

    'H': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'I': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0]],

    'J': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0],
          [0,1,1,0,1,0,0],
          [0,1,1,0,1,0,0],
          [0,1,1,1,1,0,0],
          [0,0,1,1,1,0,0]],
          
    'K': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,1,0,0],
          [0,1,1,1,0,0,0],
          [0,1,1,1,0,0,0],
          [0,1,1,0,1,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],
          
    'L': [[0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,0,0,0,0],
      [0,1,1,1,1,1,0],
      [0,1,1,1,1,1,0],
      [0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0]],
          
             
    'M': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'N': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,0,1,0],
          [0,1,0,1,1,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,1,0,1,0,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'O': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'P': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,0,0],
          [0,1,1,1,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'Q': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,1,1,0],
          [0,1,1,0,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,0,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'R': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,0,0],
          [0,1,1,1,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'S': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,0,1,1,1,0,0],
          [0,0,0,0,1,1,0],
          [0,0,0,0,0,1,0],
          [0,0,0,0,0,1,0],
          [0,0,0,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'T': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'U': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'V': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,0,1,0,0,1,0],
          [0,0,1,0,0,1,0],
          [0,0,1,0,0,1,0],
          [0,0,1,1,1,1,0],
          [0,0,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'W': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'X': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'Y': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,1,1,0,0,1,0],
          [0,0,1,1,1,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]],

    'Z': [[0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,1,1,0],
          [0,0,0,1,1,0,0],
          [0,0,1,1,0,0,0],
          [0,0,1,1,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,0,0,0,0],
          [0,1,1,1,1,1,0],
          [0,1,1,1,1,1,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]]


}

# Constants for LED matrix size
ROW_SIZE = 16
COL_SIZE = 32

# Initialize LED matrix and SPI configuration
config = hub75.Hub75SpiConfiguration()
matrix = matrixdata.MatrixData(ROW_SIZE, COL_SIZE)
hub75spi = hub75.Hub75Spi(matrix, config)

# Clear dirty bytes in matrix
matrix.clear_dirty_bytes()

# Function to display a single letter on the LED matrix
def displayLetter(letter):
    matrix.set_pixels(0, 0, numpy.array(letters[letter], dtype=numpy.uint8))
    hub75spi.display_data()

# Function to display a string of letters on the LED matrix
def displayString(string):
    valid_chars = [char.upper() for char in string if char.upper() in letters]
    arrays = [numpy.array(letters[char], dtype=numpy.uint8) for char in valid_chars]
    concatenated_array = arrays[0]
    for array in arrays[1:]:
        concatenated_array = numpy.concatenate((concatenated_array, array), axis=1)
    while True:
        matrix.set_pixels(0, 0, concatenated_array)
        hub75spi.display_data()



# Display a string of letters
displayString("RUSHIL")
