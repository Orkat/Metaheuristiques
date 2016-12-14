import math

from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.graph_objs import *

class Function_nd:


    def __init__(self):
        pass


    def get_image(self, x):
        0.0


    def plot_function_2D(self, limits, step):

        x_min = limits[0][0]
        x_max = limits[0][1]
        y_min = limits[1][0]
        y_max = limits[1][1]

        n_x = math.ceil((x_max - x_min) / float(step))
        n_y = math.ceil((y_max - y_min) / float(step))

        x_values = []
        y_values = []

        for i in range(0, n_x):
            x_values.append(x_min + float(i)*step)

        for j in range(0, n_y):
            y_values.append(y_min + float(j)*step)

        z_values = []
        for y in y_values:
            local_z = []
            for x in x_values:
                local_z.append(self.get_image([float(x), float(y)]))
            z_values.append(local_z)


        data = [Surface(z=z_values, colorscale='Viridis', x=x_values, y=y_values, lighting=dict(specular=0.1))]
        #data = [Surface(z=z_values, x=x_values, y=y_values, lighting=dict(specular=0.1))]

        layout = Layout(
            width=800,
            height=700
        )

        fig = dict(data=data, layout=layout)
        iplot(fig)


    def plot_function_2D_trace(self, limits, step, vectors_2d):

        x_min = limits[0][0]
        x_max = limits[0][1]
        y_min = limits[1][0]
        y_max = limits[1][1]

        n_x = math.ceil((x_max - x_min) / float(step))
        n_y = math.ceil((y_max - y_min) / float(step))

        x_values = []
        y_values = []

        for i in range(0, n_x):
            x_values.append(x_min + float(i)*step)

        for j in range(0, n_y):
            y_values.append(y_min + float(j)*step)

        z_values = []
        for y in y_values:
            local_z = []
            for x in x_values:
                local_z.append(self.get_image([float(x), float(y)]))
            z_values.append(local_z)

        x_values_trace = []
        y_values_trace = []
        z_values_trace = []

        for vector_2d in vectors_2d:
            x_values_trace.append(vector_2d[0])
            y_values_trace.append(vector_2d[1])
            z_values_trace.append(self.get_image(vector_2d))


        data = [
                Surface(z=z_values, colorscale='Viridis', x=x_values, y=y_values, lighting=dict(specular=0.1)),
                Scatter3d(x=x_values_trace, y=y_values_trace, z=z_values_trace, marker=dict(size=1,color='black',colorscale='Viridis'),
                          line=dict(color='black',width=1))
               ]


        layout = Layout(
            width=800,
            height=700
        )

        fig = dict(data=data, layout=layout)
        iplot(fig)
