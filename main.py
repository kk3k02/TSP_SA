from ReadINI import ReadINI
from ReadFile import ReadFile
from SimulatedAnnealing import SimulatedAnnealing




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
#best_solution, best_distance = simulated_annealing(distance_matrix)
#print("Najlepsza trasa:", best_solution)
#print("Długość trasy:", best_distance)

iniPath = "test.INI"
readIni = ReadINI(iniPath)
file_names, repeats = readIni.read_data()

for i in range(0, len(file_names)):
    readFile = ReadFile(file_names[i])
    graph = readFile.read_data()
    sa = SimulatedAnnealing(graph)
    best_solution, best_distance = sa.start()
    print("Najlepsza trasa:", best_solution)
    print("Długość trasy:", best_distance)
