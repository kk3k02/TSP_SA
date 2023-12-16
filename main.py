from ReadINI import ReadINI
from ReadFile import ReadFile
from TimeStamp import TimeStamp
from SimulatedAnnealing import SimulatedAnnealing
from Temperature import Temperature


def main():
    # SA alg. settings
    num_iterations = 100000
    cooling_rate = 0.95

    iniPath = "test.INI"
    reader = ReadINI(iniPath)
    file_names, repeats, results = reader.read_data()
    timestamp = TimeStamp()

    for i in range(0, len(file_names)):
        print("========================================================")

        graph = ReadFile(file_names[i])
        temp = Temperature(graph)
        init_temp = temp.find_initial_temperature()

        print("|>", file_names[i])
        print()

        errors = 0.0

        print("Geometric cooling | Swap neighbor:")

        for j in range(repeats[i]):
            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, num_iterations)

            timestamp.start()
            best_solution, best_distance = sa.start("geo", "swap")
            result = timestamp.end()
            print(result)

            if best_distance != results[i]:
                errors = errors + ((best_distance - results[i]) / results[i])

        print("Error rate: ", (errors / repeats[i]) * 100, "%")
        print()

        print("Geometric cooling | Rotation neighbor:")

        errors = 0.0

        for j in range(repeats[i]):
            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)

            timestamp.start()
            best_solution, best_distance = sa.start("geo", "rotation")
            result = timestamp.end()
            print(result)

            if best_distance != results[i]:
                errors = errors + (best_distance - results[i]) / results[i]

        print("Error rate: ", (errors / repeats[i]) * 100, "%")
        print()

        print("Logarithmic cooling | Swap neighbor:")

        errors = 0.0

        for j in range(repeats[i]):
            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)

            timestamp.start()
            best_solution, best_distance = sa.start("log", "swap")
            result = timestamp.end()
            print(result)

            if best_distance != results[i]:
                errors = errors + ((best_distance - results[i]) / results[i])

        print("Error rate: ", (errors / repeats[i]) * 100, "%")
        print()

        print("Logarithmic cooling | Rotation neighbor:")

        errors = 0.0

        for j in range(repeats[i]):
            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)

            timestamp.start()
            best_solution, best_distance = sa.start("log", "rotation")
            result = timestamp.end()
            print(result)

            if best_distance != results[i]:
                errors = errors + ((best_distance - results[i]) / results[i])

        print("Error rate: ", (errors / repeats[i]) * 100, "%")
        print()


if __name__ == "__main__":
    main()
