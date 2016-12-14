import definitions
import model

import math


class Schwefel(model.function_nd.Function_nd):


    def __init__(self):
        super().__init__()


    def get_image(self, x):
        return -x[0]*math.sin(math.sqrt(math.fabs(x[0]))) - x[1]*math.sin(math.sqrt(math.fabs(x[1])))
