import definitions
import model

import math


class Zakharov(model.function_nd.Function_nd):


    def __init__(self):
        super().__init__()


    def get_image(self, x):

        val1 = math.pow(x[0], 2) + math.pow(x[1], 2)
        val2 = math.pow(0.5*1.0*x[0] + 0.5*2.0*x[1], 2)
        val3 = math.pow(0.5*1.0*x[0] + 0.5*2.0*x[1], 4)

        return val1 + val2 + val3
