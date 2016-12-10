import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = ROOT_DIR + "/data/"
SRC_DIR = ROOT_DIR + "/src/"

sys.path.insert(0, SRC_DIR)
for name in os.listdir(SRC_DIR):
    if os.path.isdir(os.path.join(SRC_DIR, name)):
        sys.path.insert(0, SRC_DIR + name)

DEFAULT_INITIAL_TEMPERATURE = 0.1
DEFAULT_ITERATIONS_SIMULATED_ANNEALING = 200
DEFAULT_N_SIMULATIONS = 1
DEFAULT_VERBOSE = False
