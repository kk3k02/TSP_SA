from ReadINI import ReadINI
from SimulatedAnnealing import SimulatedAnnealing
from Temperature import Temperature
from Graph import Graph


def main():
    # Init Temp settings
    acceptable_rate = 0.95
    num_trials = 10

    # SA alg. settings
    num_iterations = 10000

    iniPath = "test.INI"
    readIni = ReadINI(iniPath)
    file_names, repeats, results = readIni.read_data()

    graph1 = Graph(file_names[0])
    print(graph1.g)

    # for i in range(0, len(file_names)):
    #     print("========================================================")
    #
    #     graph = Graph(file_names[i])
    #     print(graph.g)
    #     print(graph.vertices)
    #     print()
    #
    #     errors = 0
    #
    #     print("====================")
    #     print("Geometric cooling | Swap neighbor:\n")
    #
    #     print(file_names[i])
    #     print("Swap")
    #
    #     for j in range(0, repeats[i]):
    #         temp = Temperature(graph, acceptable_rate, num_trials, "swap")
    #         init_temp = temp.find_initial_temperature()
    #
    #         sa = SimulatedAnnealing(graph.g, init_temp, 0.999, num_iterations)
    #         best_solution, best_distance = sa.start("geo", "swap")
    #
    #         if best_distance != results[i]:
    #             errors = errors + 1
    #
    #     print("Error rate: ", (errors / repeats[i])*100, "%")
    #     print()
    #
    #     print("====================")
    #     print("Geometric cooling | Rotation neighbor:\n")
    #
    #     errors = 0
    #
    #     print(file_names[i])
    #     print("Rotation")
    #
    #     for j in range(0, repeats[i]):
    #         temp = Temperature(graph, acceptable_rate, num_trials, "rotation")
    #         init_temp = temp.find_initial_temperature()
    #
    #         sa = SimulatedAnnealing(graph.g, init_temp, 0.995, 10000)
    #         best_solution, best_distance = sa.start("geo", "rotation")
    #
    #         if best_distance != results[i]:
    #             errors = errors + 1
    #
    #     print("Error rate: ", (errors / repeats[i]) * 100, "%")
    #     print()
    #
    #
    #     print("====================")
    #     print("Logarithmic cooling | Swap neighbor:\n")
    #
    #     errors = 0
    #
    #     print(file_names[i])
    #     print("Swap")
    #
    #     for j in range(0, repeats[i]):
    #         temp = Temperature(graph, acceptable_rate, num_trials, "swap")
    #         init_temp = temp.find_initial_temperature()
    #
    #         sa = SimulatedAnnealing(graph.g, init_temp, 0.995, 10000)
    #         best_solution, best_distance = sa.start("log", "swap")
    #
    #         if best_distance != results[i]:
    #             errors = errors + 1
    #
    #     print("Error rate: ", (errors / repeats[i])*100, "%")
    #     print()
    #
    #     print("====================")
    #     print("Logarithmic cooling | Rotation neighbor:\n")
    #
    #     errors = 0
    #
    #     print(file_names[i])
    #     print("Rotation")
    #
    #     for j in range(0, repeats[i]):
    #         temp = Temperature(graph, acceptable_rate, num_trials, "rotation")
    #         init_temp = temp.find_initial_temperature()
    #
    #         sa = SimulatedAnnealing(graph.g, init_temp, 0.995, 10000)
    #         best_solution, best_distance = sa.start("log", "rotation")
    #
    #         if best_distance != results[i]:
    #             errors = errors + 1
    #
    #     print("Error rate: ", (errors / repeats[i])*100, "%")
    #     print()

if __name__ == "__main__":
    main()
