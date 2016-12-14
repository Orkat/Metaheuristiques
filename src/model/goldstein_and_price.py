import definitions
import model

import math



class GoldsteinAndPrice(model.function_nd.Function_nd):


    def __init__(self):
        super().__init__()


    def get_image(self, x):

        val1 = 1.0 + math.pow(x[0]+x[1]+1.0,2)*(19.0-14.0*x[0]+3.0*math.pow(x[0],2)-14.0*x[1]+6.0*x[0]*x[1]+3.0*math.pow(x[1],2))
        val2 = 30.0 + math.pow(2.0*x[0]-3.0*x[1], 2)*(18.0-32.0*x[0]+12.0*math.pow(x[0],2)+48.0*x[1]-36.0*x[0]*x[1]+27.0*math.pow(x[1],2))

        return val1*val2
