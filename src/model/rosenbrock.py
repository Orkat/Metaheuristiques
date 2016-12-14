import definitions
import model

import math


class Rosenbrock(model.function_nd.Function_nd):


    def __init__(self):
        super().__init__()


    def get_image(self, x):
        return 100.0*math.pow(x[1] - math.pow(x[0], 2), 2) + math.pow(x[1] - 1.0, 2)
