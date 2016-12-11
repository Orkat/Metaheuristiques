import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import random

import common


class CircuitNode:



    def __init__(self):
        self.connections = []


    def add_connection(self, other_node):
        self.connections.append(other_node)


    def set_index(self, index):
        self.index = index

    def set_position_index(self, position_index):
        self.position_index = position_index




class Circuit:


    def __init__(self, n_side):

        self.n_side = n_side
        self.n_nodes = n_side*n_side

        self.nodes = []
        for i in range(0, self.n_nodes):
            circuit_node = CircuitNode()
            circuit_node.set_index(i)
            circuit_node.set_position_index(i)
            self.nodes.append(circuit_node)

        for i in range(0, n_side):
            for j in range(0, n_side):
                current_index = i*n_side + j
                if i > 0:
                    self.nodes[current_index].add_connection(self.nodes[current_index-n_side])
                if i < n_side - 1:
                    self.nodes[current_index].add_connection(self.nodes[current_index+n_side])
                if j > 0:
                    self.nodes[current_index].add_connection(self.nodes[current_index-1])
                if j < n_side - 1:
                    self.nodes[current_index].add_connection(self.nodes[current_index+1])

        self.factorial_n_nodes = math.factorial(self.n_nodes)



    def perform_random_permutation(self):

        alist = []

        for i in range(0, self.n_nodes):
            index = random.randint(0, self.n_nodes - 1)
            while index in alist:
                index = random.randint(0, self.n_nodes - 1)
            alist.append(index)

        for i in range(0, self.n_nodes):
            self.nodes[i].position_index = alist[i]


    def permute(self, seed):

        alist = list(range(0, self.n_nodes))
        alist = common.utils.perm_given_index(alist, seed % self.factorial_n_nodes)
        for i in range(0, self.n_nodes):
            self.nodes[i].position_index = alist[i]



    def perform_random_swap(self):

        i = random.randint(0, self.n_nodes - 1)
        j = i
        while j == i:
            j = random.randint(0, self.n_nodes - 1)

        self.swap(i, j)



    def swap(self, i, j):

        tmp = self.nodes[i].position_index
        self.nodes[i].position_index = self.nodes[j].position_index
        self.nodes[j].position_index = tmp



    def plot(self, margin=0.1, interval_ratio=0.5):

        axis = plt.gca()
        axis.set_xlim([0.0, 1.0])
        axis.set_ylim([0.0, 1.0])

        rect_width = self.get_rect_width(margin, interval_ratio)

        for i in range(0, self.n_nodes):
            position_index_i = self.nodes[i].position_index
            x, y = self.index_to_coordinates(position_index_i, margin, interval_ratio)
            axis.add_patch(patches.Rectangle((x, y), rect_width, rect_width, fill=False))
            for j in range(0, len(self.nodes[i].connections)):
                position_index_j = self.nodes[i].connections[j].position_index
                if position_index_i < position_index_j:
                    x_prime, y_prime = self.index_to_coordinates(position_index_j, margin, interval_ratio)
                    plt.plot([x+rect_width/2, x_prime+rect_width/2], [y+rect_width/2, y_prime+rect_width/2], 'k-', lw=1)

        plt.show()



    def index_to_coordinates(self, index, margin, interval_ratio):

        rect_width = self.get_rect_width(margin, interval_ratio)

        i = index // self.n_side
        j = index % self.n_side

        x = margin + j*rect_width
        y = margin + i*rect_width

        if j > 0:
            x += j*rect_width*interval_ratio

        if i > 0:
            y += i*rect_width*interval_ratio

        return x, y



    def get_rect_width(self, margin, interval_ratio):

        return (1.0 - 2.0*margin) / (self.n_side + (self.n_side-1.0)*interval_ratio)



    def calculate_configuration_length(self):

        total_length = 0
        for i in range(0, self.n_nodes):

            position_index_i = self.nodes[i].position_index

            x_i = position_index_i // self.n_side
            y_i = position_index_i % self.n_side

            for j in range(0, len(self.nodes[i].connections)):

                position_index_j = self.nodes[i].connections[j].position_index

                if position_index_i < position_index_j:

                    x_j = position_index_j // self.n_side
                    y_j = position_index_j % self.n_side

                    dist_x = x_i - x_j
                    dist_y = y_i - y_j

                    total_length += math.sqrt(dist_x*dist_x + dist_y*dist_y)

        return total_length*5
