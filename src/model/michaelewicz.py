import definitions
import model

import math


class Michaelewicz(model.function_nd.Function_nd):

    def __init__(self):
        super().__init__()

    '''
    x is array of dimension n
    '''
    def get_image(self, x):

        ret = 0.0
        n = len(x)

        for i in range(1, n+1):
            ret -= math.sin(x[i-1])*math.pow(math.sin((float(i)*math.pow(x[i-1], 2))/math.pi), 20)

        return ret
