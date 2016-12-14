import definitions
import model

import math



class DeJongF2(model.function_nd.Function_nd):


    def __init__(self):
        super().__init__()


    def get_image(self, x):
        return 100.0*math.pow((math.pow(x[1], 2.0) - x[0]), 2) + math.pow((1.0 - x[0]), 2)
