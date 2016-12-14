import definitions
import model

import math



class DeJongF3(model.function_nd.Function_nd):


    def __init__(self):
        super().__init__()


    def get_image(self, x):
        return 25.0 + math.floor(x[0]) + math.floor(x[1])
