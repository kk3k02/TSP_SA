from ReadINI import ReadINI
from ReadFile import ReadFile
from SimulatedAnnealing import SimulatedAnnealing
from Temperature import Temperature


def main():
    # Init Temp settings
    acceptable_rate = 0.95
    num_trials = 10

    iniPath = "test.INI"
    readIni = ReadINI(iniPath)
    file_names, repeats, results = readIni.read_data()

    print("====================")
    print("Geometric cooling | Swap neighbor:\n")

    for i in range(0, len(file_names)):
        readFile = ReadFile(file_names[i])
        graph = readFile.read_data()

        temp = Temperature(graph, acceptable_rate, num_trials, "swap")
        init_temp = temp.find_initial_temperature()

        sa = SimulatedAnnealing(graph, init_temp, 0.995, 10000)
        best_solution, best_distance = sa.start("geo", "swap")
        print(file_names[i])
        print("Najlepsza trasa:", best_solution)
        print("Długość trasy:", best_distance)
        if best_distance == results[i]:
            print("OK")
        else:
            print("NOT OK")
        print()

    print("====================")
    print("Geometric cooling | Rotation neighbor:\n")

    for i in range(0, len(file_names)):
        readFile = ReadFile(file_names[i])
        graph = readFile.read_data()

        temp = Temperature(graph, acceptable_rate, num_trials, "rotation")
        init_temp = temp.find_initial_temperature()

        sa = SimulatedAnnealing(graph, init_temp, 0.995, 10000)
        best_solution, best_distance = sa.start("geo", "rotation")
        print(file_names[i])
        print("Najlepsza trasa:", best_solution)
        print("Długość trasy:", best_distance)
        if best_distance == results[i]:
            print("OK")
        else:
            print("NOT OK")
        print()

    print("====================")
    print("Logarithmic cooling | Swap neighbor:\n")

    for i in range(0, len(file_names)):
        readFile = ReadFile(file_names[i])
        graph = readFile.read_data()

        temp = Temperature(graph, acceptable_rate, num_trials, "swap")
        init_temp = temp.find_initial_temperature()

        sa = SimulatedAnnealing(graph, init_temp, 0.995, 10000)
        best_solution, best_distance = sa.start("log", "swap")
        print(file_names[i])
        print("Najlepsza trasa:", best_solution)
        print("Długość trasy:", best_distance)
        if best_distance == results[i]:
            print("OK")
        else:
            print("NOT OK")
        print()

    print("====================")
    print("Logarithmic cooling | Rotation neighbor:\n")

    for i in range(0, len(file_names)):
        readFile = ReadFile(file_names[i])
        graph = readFile.read_data()

        temp = Temperature(graph, acceptable_rate, num_trials, "rotation")
        init_temp = temp.find_initial_temperature()

        sa = SimulatedAnnealing(graph, init_temp, 0.995, 10000)
        best_solution, best_distance = sa.start("log", "rotation")
        print(file_names[i])
        print("Najlepsza trasa:", best_solution)
        print("Długość trasy:", best_distance)
        if best_distance == results[i]:
            print("OK")
        else:
            print("NOT OK")
        print()


if __name__ == "__main__":
    main()
