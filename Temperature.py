import math
import random
from SimulatedAnnealing import SimulatedAnnealing

class Temperature:

    def __init__(self, graph, acceptable_rate, num_trials, neighbor_method):
        self.sa_instance = SimulatedAnnealing(graph, 1000, 0.995, 10000)
        self.acceptable_rate = acceptable_rate
        self.num_trials = num_trials
        self.neighbor_method = neighbor_method

    def find_initial_temperature(self):
        num_cities = len(self.sa_instance.distance_matrix)
        total_trials = 0
        total_accepted = 0

        for _ in range(self.num_trials):
            current_solution = self.sa_instance.generate_initial_solution(num_cities)
            current_distance = self.sa_instance.calculate_total_distance(current_solution)

            for iteration in range(num_cities):
                if self.neighbor_method == "swap":
                    neighbor_solution = self.sa_instance.generate_neighbor_solution_swap(current_solution)
                if self.neighbor_method == "rotation":
                    neighbor_solution = self.sa_instance.generate_neighbor_solution_rotation(current_solution)
                new_distance = self.sa_instance.calculate_total_distance(neighbor_solution)

                acceptance_prob = self.sa_instance.acceptance_probability(
                    current_distance, new_distance, self.sa_instance.geometric_cooling(
                        self.sa_instance.initial_temperature,  # Poprawka: użycie początkowej temperatury
                        0.995, iteration
                    )
                )

                if acceptance_prob > random.random():
                    total_accepted += 1

                total_trials += 1

        average_acceptance_rate = total_accepted / total_trials

        if average_acceptance_rate == 0:
            return float('inf')

        initial_temperature = -math.log(self.acceptable_rate) * current_distance / (
                self.sa_instance.initial_temperature * average_acceptance_rate
        )

        return initial_temperature
