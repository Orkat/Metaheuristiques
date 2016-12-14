import math
import random
import matplotlib.pyplot as plt

import common
import model
import algorithm



class GeneticAlgorithmConvergence():



    def __init__(self):
        pass



    def perform_simulation(self, pool_size, vector_size, vector_limits, evaluation_function,
                           mutation_rate, selection_size, max_iterations):

        self.evaluation_function = evaluation_function

        genetic_algorithm = algorithm.genetic_algorithm.GeneticAlgorithm(pool_size, vector_size, vector_limits, evaluation_function)
        genetic_algorithm.run_algorithm(mutation_rate, selection_size, max_iterations, True)

        self.convergence = genetic_algorithm.convergence



    def perform_multiple_simulations(self, pool_size, vector_size, vector_limits, evaluation_function,
                                     mutation_rate, selection_size, max_iterations, n_simulations):

        self.multiple_convergence = []
        self.final_values = {}
        self.evaluation_function = evaluation_function

        for i in range(0, n_simulations):
            genetic_algorithm = algorithm.genetic_algorithm.GeneticAlgorithm(pool_size, vector_size, vector_limits, evaluation_function)
            genetic_algorithm.run_algorithm(mutation_rate, selection_size, max_iterations, True)
            self.multiple_convergence.append(genetic_algorithm.convergence)
            final_value = genetic_algorithm.convergence[-1][1]
            if final_value not in self.final_values:
                self.final_values[final_value] = 1
            else:
                self.final_values[final_value] += 1



    def perform_multiple_simulations_mutation_rate(self, pool_size, vector_size, vector_limits, evaluation_function,
                                                   mutation_rates, selection_size, max_iterations, n_simulations):

        self.multiple_convergence_mutation_rates = []
        self.final_values_mutation_rates = []
        self.mutation_rates = mutation_rates
        self.evaluation_function = evaluation_function

        for mutation_rate in mutation_rates:

            multiple_convergence = []
            final_values = {}

            for i in range(0, n_simulations):
                genetic_algorithm = algorithm.genetic_algorithm.GeneticAlgorithm(pool_size, vector_size, vector_limits, evaluation_function)
                genetic_algorithm.run_algorithm(mutation_rate, selection_size, max_iterations, True)
                multiple_convergence.append(genetic_algorithm.convergence)
                final_value = genetic_algorithm.convergence[-1][1]
                if final_value not in final_values:
                    final_values[final_value] = 1
                else:
                    final_values[final_value] += 1

            self.multiple_convergence_mutation_rates.append(multiple_convergence)
            self.final_values_mutation_rates.append(final_values)



    def plot_convergence(self):

        x_values = []
        y_values = []

        for i in range(0, len(self.convergence)):
            x_values.append(i)
            y_values.append(self.convergence[i][1])

        plt.plot(x_values, y_values)
        plt.xlabel('epochs', fontsize=18)
        plt.ylabel('solution value', fontsize=18)
        plt.show()



    def plot_convergence_surface(self, limits, step):

        vectors_2d = []
        for i in range(0, len(self.convergence)):
            vectors_2d.append(self.convergence[i][0])

        self.evaluation_function.plot_function_2D_trace(limits, step, vectors_2d)



    def plot_multiple_convergence(self, axis_lim=None):


        for i in range(0, len(self.multiple_convergence)):

            convergence = self.multiple_convergence[i]

            x_values = []
            y_values = []

            for i in range(0, len(convergence)):
                x_values.append(i)
                y_values.append(convergence[i][1])

            plt.plot(x_values, y_values, color='orange', alpha=0.5)


        self.average_convergence = [0] * len(self.multiple_convergence[0])
        for i in range(0, len(self.multiple_convergence)):
            convergence = self.multiple_convergence[i]
            for j in range(0, len(convergence)):
                self.average_convergence[j] += float(convergence[j][1]) / float(len(self.multiple_convergence))

        x_values = []
        y_values = []

        for i in range(0, len(self.average_convergence)):
            x_values.append(i)
            y_values.append(self.average_convergence[i])

        plt.plot(x_values, y_values, color='blue', linewidth=2)

        if axis_lim is not None:
            plt.axis(axis_lim)
        plt.xlabel('epochs', fontsize=18)
        plt.ylabel('solution value', fontsize=18)
        plt.show()



    def plot_multiple_convergence_mutation_rates(self, axis_lim=None):

        self.average_convergence_mutation_rates = []

        lines = []

        for j in range(0, len(self.mutation_rates)):

            if axis_lim is None:
                average_convergence = [0] * len(self.multiple_convergence_mutation_rates[j][0])
                for i in range(0, len(self.multiple_convergence_mutation_rates[j])):
                    convergence = self.multiple_convergence_mutation_rates[j][i]
                    for k in range(0, len(convergence)):
                        average_convergence[k] += float(convergence[k][1]) / float(len(self.multiple_convergence_mutation_rates[j]))
            else:
                x_min = max(0, axis_lim[0])
                x_max = min(len(self.multiple_convergence_mutation_rates[j][0]), axis_lim[1])
                average_convergence = [0] * (x_max - x_min + 1)
                for i in range(0, len(self.multiple_convergence_mutation_rates[j])):
                    convergence = self.multiple_convergence_mutation_rates[j][i]
                    for k in range(0, x_max - x_min):
                        average_convergence[k] += float(convergence[k+x_min][1]) / float(len(self.multiple_convergence_mutation_rates[j]))

            self.average_convergence_mutation_rates.append(average_convergence)

            x_values = []
            y_values = []

            for i in range(0, len(average_convergence)):
                x_values.append(i)
                y_values.append(average_convergence[i])


            line, = plt.plot(x_values, y_values, linewidth=2, label=str(self.mutation_rates[j]))
            lines.append(line)


        if axis_lim is not None:
            plt.axis(axis_lim)
        plt.xlabel('epochs', fontsize=18)
        plt.ylabel('solution value', fontsize=18)
        plt.legend(handles=lines)
        plt.show()
