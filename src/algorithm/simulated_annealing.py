import math
import random
import copy

import common
import model



class SimulatedAnnealing:



    def __init__(self):
        pass



    def initialise(self, n_side, seed_value, initial_temperature):

        self.n_side = n_side
        self.n_nodes = n_side*n_side
        self.n_nodes_factorial = math.factorial(self.n_nodes)

        self.seed_value = seed_value
        self.circuit = model.circuit.Circuit(n_side)
        #self.circuit.permute(seed_value)
        self.circuit.perform_random_permutation()
        self.circuit_configuration_length = self.circuit.calculate_configuration_length()

        self.initial_temperature = float(initial_temperature)
        self.temperature = float(initial_temperature)



    def run_algorithm(self, max_iterations, save_convergence=False, save_circuits=False, save_n_iterations=100):

        if save_convergence:
            self.convergence = []
            self.convergence.append(self.circuit_configuration_length)

        if save_circuits:
            self.saved_circuits = []
            self.saved_circuits_configuration_lengths = []
            self.saved_circuits.append(copy.deepcopy(self.circuit))
            self.saved_circuits_configuration_lengths.append(self.circuit_configuration_length)

        running = True
        current_iteration = 0
        while running:

            circuit, configuration_length = self.get_neighbour_circuit_configuration_length()
            if self.get_acceptance_probability(configuration_length) >= random.random():
                self.circuit = circuit
                self.circuit_configuration_length = configuration_length
            self.lower_temperature(float(current_iteration) / float(max_iterations))

            if save_convergence:
                self.convergence.append(self.circuit_configuration_length)

            if save_circuits and (current_iteration+1) % save_n_iterations == 0:
                self.saved_circuits.append(copy.deepcopy(self.circuit))
                self.saved_circuits_configuration_lengths.append(self.circuit_configuration_length)

            current_iteration += 1
            if current_iteration >= max_iterations:
                running = False

        return self.circuit



    def get_neighbour_circuit_configuration_length(self):

        circuit = copy.deepcopy(self.circuit)
        circuit.perform_random_swap()
        configuration_length = circuit.calculate_configuration_length()

        return circuit, configuration_length



    def get_acceptance_probability(self, configuration_length):

        if -(float(configuration_length) - float(self.circuit_configuration_length))/float(self.temperature) > 10.0:
            return 1.0

        return math.exp(-(float(configuration_length) - float(self.circuit_configuration_length))/float(self.temperature))



    def lower_temperature(self, progress):

        self.temperature = self.initial_temperature * (1.0 - progress)
