import math
import random
import matplotlib.pyplot as plt

import common
import model
import algorithm


class SimulatedAnnealingConvergence():


    def __init__(self):
        pass


    def perform_simulation(self, n_side, seed_value, initial_temperature, max_iterations):

        simulated_annealing = algorithm.simulated_annealing.SimulatedAnnealing()
        simulated_annealing.initialise(n_side, seed_value, initial_temperature)
        simulated_annealing.run_algorithm(max_iterations, True)

        self.convergence = simulated_annealing.convergence


    def perform_multiple_simulations(self, n_side, initial_temperature, max_iterations, n_simulations):

        self.multiple_convergence = []
        self.final_values = {}

        n_nodes_factorial = math.factorial(n_side*n_side)

        for i in range(0, n_simulations):
            seed_value = random.randint(0, n_nodes_factorial - 1)
            simulated_annealing = algorithm.simulated_annealing.SimulatedAnnealing()
            simulated_annealing.initialise(n_side, seed_value, initial_temperature)
            simulated_annealing.run_algorithm(max_iterations, True)
            self.multiple_convergence.append(simulated_annealing.convergence)
            final_value = simulated_annealing.convergence[-1]
            if final_value not in self.final_values:
                self.final_values[final_value] = 1
            else:
                self.final_values[final_value] += 1


    def perform_multiple_simulations_initial_temperatures(self, n_side, initial_temperatures, max_iterations, n_simulations):

        self.multiple_convergence_temperatures = []
        self.final_values_temperatures = []
        self.initial_temperatures = initial_temperatures

        n_nodes_factorial = math.factorial(n_side*n_side)

        for initial_temperature in initial_temperatures:

            multiple_convergence = []
            final_values = {}

            for i in range(0, n_simulations):
                seed_value = random.randint(0, n_nodes_factorial - 1)
                simulated_annealing = algorithm.simulated_annealing.SimulatedAnnealing()
                simulated_annealing.initialise(n_side, seed_value, initial_temperature)
                simulated_annealing.run_algorithm(max_iterations, True)
                multiple_convergence.append(simulated_annealing.convergence)
                final_value = simulated_annealing.convergence[-1]
                if final_value not in final_values:
                    final_values[final_value] = 1
                else:
                    final_values[final_value] += 1

            self.multiple_convergence_temperatures.append(multiple_convergence)
            self.final_values_temperatures.append(final_values)



    def plot_convergence(self):

        x_values = []
        y_values = []

        for i in range(0, len(self.convergence)):
            x_values.append(i)
            y_values.append(self.convergence[i])

        plt.plot(x_values, y_values)
        plt.xlabel('iterations', fontsize=18)
        plt.ylabel('configuration length', fontsize=18)
        plt.show()


    def plot_multiple_convergence(self):


        for i in range(0, len(self.multiple_convergence)):

            convergence = self.multiple_convergence[i]

            x_values = []
            y_values = []

            for i in range(0, len(convergence)):
                x_values.append(i)
                y_values.append(convergence[i])

            plt.plot(x_values, y_values, color='orange', alpha=0.5)


        self.average_convergence = [0] * len(self.multiple_convergence[0])
        for i in range(0, len(self.multiple_convergence)):
            convergence = self.multiple_convergence[i]
            for j in range(0, len(convergence)):
                self.average_convergence[j] += float(convergence[j]) / float(len(self.multiple_convergence))

        x_values = []
        y_values = []

        for i in range(0, len(self.average_convergence)):
            x_values.append(i)
            y_values.append(self.average_convergence[i])

        plt.plot(x_values, y_values, color='blue', linewidth=2)


        plt.xlabel('iterations', fontsize=18)
        plt.ylabel('configuration length', fontsize=18)
        plt.show()



    def plot_multiple_convergence_initial_temperatures(self, axis_lim=None):

        self.average_convergence_temperatures = []

        lines = []

        for j in range(0, len(self.initial_temperatures)):

            if axis_lim is None:
                average_convergence = [0] * len(self.multiple_convergence_temperatures[j][0])
                for i in range(0, len(self.multiple_convergence_temperatures[j])):
                    convergence = self.multiple_convergence_temperatures[j][i]
                    for k in range(0, len(convergence)):
                        average_convergence[k] += float(convergence[k]) / float(len(self.multiple_convergence_temperatures[j]))
            else:
                x_min = max(0, axis_lim[0])
                x_max = min(len(self.multiple_convergence_temperatures[j][0]), axis_lim[1])
                average_convergence = [0] * (x_max - x_min + 1)
                for i in range(0, len(self.multiple_convergence_temperatures[j])):
                    convergence = self.multiple_convergence_temperatures[j][i]
                    for k in range(0, x_max - x_min + 1):
                        average_convergence[k] += float(convergence[k+x_min]) / float(len(self.multiple_convergence_temperatures[j]))

            self.average_convergence_temperatures.append(average_convergence)

            x_values = []
            y_values = []

            if axis_lim is None:
                for i in range(0, len(average_convergence)):
                    x_values.append(i)
                    y_values.append(average_convergence[i])
            else:
                for i in range(0, len(average_convergence)):
                    x_values.append(i + axis_lim[0])
                    y_values.append(average_convergence[i])

            line, = plt.plot(x_values, y_values, linewidth=2, label=str(self.initial_temperatures[j]))
            lines.append(line)


        if axis_lim is not None:
            plt.axis(axis_lim)
        plt.xlabel('iterations', fontsize=18)
        plt.ylabel('configuration length', fontsize=18)
        plt.legend(handles=lines)
        plt.show()



    def plot_best_multiple_convergence_initial_temperatures(self, n_best, axis_lim=None):

        self.average_convergence_temperatures = []

        lines = []

        for j in range(0, len(self.initial_temperatures)):

            best_convergences = [[] for i in range(0, len(self.multiple_convergence_temperatures[j][0]))]
            for i in range(0, len(self.multiple_convergence_temperatures[j])):
                for p in range(0, len(self.multiple_convergence_temperatures[j][0])):
                    if len(best_convergences[p]) <= n_best:
                        best_convergences[p].append(self.multiple_convergence_temperatures[j][i][p])
                    else:
                        for k in range(0, n_best):
                            if self.multiple_convergence_temperatures[j][i][p] < best_convergences[p][k]:
                                best_convergences[p][k] = self.multiple_convergence_temperatures[j][i][p]
                                break

            if axis_lim is None:
                average_convergence = [0] * len(best_convergences)
                for i in range(0, len(best_convergences)):
                    for k in range(0, len(best_convergences[i])):
                        average_convergence[i] += float(best_convergences[i][k]) / float(len(best_convergences[i]))
            else:
                x_min = max(0, axis_lim[0])
                x_max = min(len(best_convergences), axis_lim[1])
                average_convergence = [0] * (x_max - x_min + 1)
                for i in range(0, x_max - x_min + 1):
                    for k in range(0, len(best_convergences[i])):
                        average_convergence[i] += float(best_convergences[i+x_min][k]) / float(len(best_convergences[i]))

            self.average_convergence_temperatures.append(average_convergence)

            x_values = []
            y_values = []

            if axis_lim is None:
                for i in range(0, len(average_convergence)):
                    x_values.append(i)
                    y_values.append(average_convergence[i])
            else:
                for i in range(0, len(average_convergence)):
                    x_values.append(i + axis_lim[0])
                    y_values.append(average_convergence[i])

            line, = plt.plot(x_values, y_values, linewidth=2, label=str(self.initial_temperatures[j]))
            lines.append(line)


        if axis_lim is not None:
            plt.axis(axis_lim)
        plt.xlabel('iterations', fontsize=18)
        plt.ylabel('configuration length', fontsize=18)
        plt.legend(handles=lines)
        plt.show()




    def plot_final_values_histogram(self):

        x_values = []
        y_values = []

        for final_value, frequency in sorted(self.final_values.items()):
            x_values.append(final_value)
            y_values.append(frequency)

        x_values.insert(0, min(x_values) - 1)
        y_values.insert(0, 0)
        x_values.append(max(x_values) + 1)
        y_values.append(0)

        plt.plot(x_values, y_values)
        plt.xlabel('final configuration length', fontsize=18)
        plt.ylabel('frequency', fontsize=18)
        plt.show()
