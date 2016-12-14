import math
import random
import numpy as np
import copy



class GeneticAlgorithm:



    def __init__(self, pool_size=100, vector_size=2, vector_limits=[[-1.0, 1.0], [-1.0, 1.0]], evaluation_function=None):

        self.pool_size = pool_size
        self.vector_size = vector_size
        self.vector_limits = vector_limits
        self.evaluation_function = evaluation_function

        self.pool = []
        for i in range(0, pool_size):
            pool_element = []
            for j in range(0, vector_size):
                value = random.random()*(vector_limits[j][1] - vector_limits[j][0]) + vector_limits[j][0]
                pool_element.append(value)
            self.pool.append(pool_element)



    def perform_epoch(self, mutation_rate=0.1, selection_size=10, save_convergence=False):

        evaluations = []
        for i in range(0, self.pool_size):
            evaluations.append(((self.evaluation_function.get_image(self.pool[i]) ), i))

        evaluations = sorted(evaluations)

        if save_convergence:
            self.convergence.append((self.pool[evaluations[0][1]], evaluations[0][0]))

        new_pool = []
        for i in range(0, selection_size):
            new_pool.append(self.pool[evaluations[i][1]])

        for i in range(selection_size, self.pool_size):
            pool_element = copy.deepcopy(new_pool[random.randint(0, selection_size-1)])
            for j in range(0, self.vector_size):
                pool_element[j] = np.random.normal(loc=pool_element[j], scale=mutation_rate)
                if pool_element[j] < self.vector_limits[j][0]:
                    pool_element[j] = self.vector_limits[j][0]
                if pool_element[j] > self.vector_limits[j][1]:
                    pool_element[j] = self.vector_limits[j][1]
            new_pool.append(pool_element)

        self.pool = new_pool

        return self.pool[0], evaluations[0][0]



    def run_algorithm(self, mutation_rate=0.1, selection_size=10, max_iterations=10, save_convergence=False):

        if save_convergence:
            self.convergence = []

        for i in range(0, max_iterations):
            best_solution, best_score = self.perform_epoch(mutation_rate, selection_size, save_convergence)

        return best_solution, best_score
