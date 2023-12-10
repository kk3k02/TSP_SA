import math
import random

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Wrapping back to the starting city
    return total_distance

def generate_initial_solution(num_cities):
    return random.sample(range(num_cities), num_cities)

def generate_neighbor_solution(current_solution):
    neighbor_solution = current_solution.copy()
    index1, index2 = random.sample(range(len(current_solution)), 2)
    neighbor_solution[index1], neighbor_solution[index2] = neighbor_solution[index2], neighbor_solution[index1]
    return neighbor_solution

def acceptance_probability(current_distance, new_distance, temperature):
    if new_distance < current_distance:
        return 1.0
    return math.exp((current_distance - new_distance) / temperature)

def simulated_annealing(distance_matrix, initial_temperature=1000, cooling_rate=0.995, num_iterations=10000):
    num_cities = len(distance_matrix)
    current_solution = generate_initial_solution(num_cities)
    current_distance = calculate_total_distance(current_solution, distance_matrix)
    best_solution = current_solution.copy()
    best_distance = current_distance

    temperature = initial_temperature

    for iteration in range(num_iterations):
        neighbor_solution = generate_neighbor_solution(current_solution)
        new_distance = calculate_total_distance(neighbor_solution, distance_matrix)

        if acceptance_probability(current_distance, new_distance, temperature) > random.random():
            current_solution = neighbor_solution
            current_distance = new_distance

        if current_distance < best_distance:
            best_solution = current_solution.copy()
            best_distance = current_distance

        temperature *= cooling_rate

    return best_solution, best_distance

# Przykładowe użycie:
# Zakładamy, że mamy macierz odległości między miastami (symetryczną):
distance_matrix = [
    [-1, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23],
    [29, -1, 55, 46, 42, 43, 43, 23, 23, 31, 41, 51, 11],
    [82, 55, -1, 68, 46, 55, 23, 43, 41, 29, 79, 21, 64],
    [46, 46, 68, -1, 82, 15, 72, 31, 62, 42, 21, 51, 51],
    [68, 42, 46, 82, -1, 74, 23, 52, 21, 46, 82, 58, 46],
    [52, 43, 55, 15, 74, -1, 61, 23, 55, 31, 33, 37, 51],
    [72, 43, 23, 72, 23, 61, -1, 42, 23, 31, 77, 37, 51],
    [42, 23, 43, 31, 52, 23, 42, -1, 33, 15, 37, 33, 33],
    [51, 23, 41, 62, 21, 55, 23, 33, -1, 29, 62, 46, 29],
    [55, 31, 29, 42, 46, 31, 31, 15, 29, -1, 51, 21, 41],
    [29, 41, 79, 21, 82, 33, 77, 37, 62, 51, -1, 65, 42],
    [74, 51, 21, 51, 58, 37, 37, 33, 46, 21, 65, -1, 61],
    [23, 11, 64, 51, 46, 51, 51, 33, 29, 41, 42, 61, -1]
]

# Wynik to najlepsze znalezione rozwiązanie (najkrótsza trasa) oraz długość tej trasy:
best_solution, best_distance = simulated_annealing(distance_matrix)
print("Najlepsza trasa:", best_solution)
print("Długość trasy:", best_distance)
