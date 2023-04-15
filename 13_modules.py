### Modules ###
#No se puede importar ficheros que empiecen con números
#import my_module
#from 10_functions import return_sum_two_values
from my_module import sumValues, printValue

#print(my_module.sumValues(1,2,3))
print(sumValues(1,2,3))

#my_module.printValue("Fuego")

printValue("Fuego")

import math

print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE#El nombre de pi lo he renombrado a PI_VALUE

print(PI_VALUE)