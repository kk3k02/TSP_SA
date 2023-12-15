from ReadINI import ReadINI
from ReadFile import ReadFile
from SimulatedAnnealing import SimulatedAnnealing
from Temperature import Temperature


def main():
    # SA alg. settings
    num_iterations = 10000
    cooling_rate = 0.999

    iniPath = "test.INI"
    reader = ReadINI(iniPath)
    file_names, repeats, results = reader.read_data()

    for i in range(0, len(file_names)):
        print("========================================================")

        file = ReadFile(file_names[i])
        graph = file.readData()
        temp = Temperature(graph, file.num_ver)

        print(file.filePath)
        print()

        errors = 0

        print("====================")
        print("Geometric cooling | Swap neighbor:\n")

        print(file_names[i])
        print("Swap")

        for j in range(0, repeats[i]):
            init_temp = temp.find_initial_temperature()

            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, num_iterations)
            best_solution, best_distance = sa.start("geo", "swap")

            if best_distance != results[i]:
                errors = errors + 1

        print("Error rate: ", (errors / repeats[i]) * 100, "%")
        print()

        print("====================")
        print("Geometric cooling | Rotation neighbor:\n")

        errors = 0

        print(file_names[i])
        print("Rotation")

        for j in range(0, repeats[i]):
            init_temp = temp.find_initial_temperature()

            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)
            best_solution, best_distance = sa.start("geo", "rotation")

            if best_distance != results[i]:
                errors = errors + 1

        print("Error rate: ", (errors / repeats[i]) * 100, "%")
        print()

        print("====================")
        print("Logarithmic cooling | Swap neighbor:\n")

        errors = 0

        print(file_names[i])
        print("Swap")

        for j in range(0, repeats[i]):
            init_temp = temp.find_initial_temperature()

            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)
            best_solution, best_distance = sa.start("log", "swap")

            if best_distance != results[i]:
                errors = errors + 1

        print("Error rate: ", (errors / repeats[i]) * 100, "%")
        print()

        print("====================")
        print("Logarithmic cooling | Rotation neighbor:\n")

        errors = 0

        print(file_names[i])
        print("Rotation")

        for j in range(0, repeats[i]):
            init_temp = temp.find_initial_temperature()

            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)
            best_solution, best_distance = sa.start("log", "rotation")

            if best_distance != results[i]:
                errors = errors + 1

        print("Error rate: ", (errors / repeats[i]) * 100, "%")
        print()


if __name__ == "__main__":
    main()
