import math
import random


def acceptance_probability(current_distance, new_distance, temperature):
    if new_distance < current_distance:
        return 1.0
    return math.exp((current_distance - new_distance) / temperature)


def generate_initial_solution(num_cities):
    return random.sample(range(num_cities), num_cities)


def generate_neighbor_solution(current_solution):
    neighbor_solution = current_solution.copy()
    index1, index2 = random.sample(range(len(current_solution)), 2)
    neighbor_solution[index1], neighbor_solution[index2] = neighbor_solution[index2], neighbor_solution[index1]
    return neighbor_solution


class SimulatedAnnealing:

    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix

    def calculate_total_distance(self, tour):
        total_distance = 0
        num_cities = len(tour)
        for i in range(num_cities - 1):
            total_distance += self.distance_matrix[tour[i]][tour[i + 1]]
        total_distance += self.distance_matrix[tour[-1]][tour[0]]  # Wrapping back to the starting city
        return total_distance

    def start(self, initial_temperature=1000, cooling_rate=0.995, num_iterations=10000):
        num_cities = len(self.distance_matrix)
        current_solution = generate_initial_solution(num_cities)
        current_distance = self.calculate_total_distance(current_solution)
        best_solution = current_solution.copy()
        best_distance = current_distance

        temperature = initial_temperature

        for iteration in range(num_iterations):
            neighbor_solution = generate_neighbor_solution(current_solution)
            new_distance = self.calculate_total_distance(neighbor_solution)

            if acceptance_probability(current_distance, new_distance, temperature) > random.random():
                current_solution = neighbor_solution
                current_distance = new_distance

            if current_distance < best_distance:
                best_solution = current_solution.copy()
                best_distance = current_distance

            temperature *= cooling_rate

        return best_solution, best_distance
