from ReadINI import ReadINI
from ReadFile import ReadFile
from TimeStamp import TimeStamp
from SimulatedAnnealing import SimulatedAnnealing
from Temperature import Temperature
from SaveToFile import SaveToFile


def main():
    # SA alg. settings
    num_iterations = 100000
    cooling_rate = 0.95

    iniPath = "test.INI"
    reader = ReadINI(iniPath)
    file_names, repeats, results = reader.read_data()
    timestamp = TimeStamp()

    schemas = ["Geometric cooling | Swap neighbor:", "Geometric cooling | Rotation neighbor:", "Logarithmic cooling | "
                                                                                               "Swap neighbor:",
               "Logarithmic cooling | Rotation neighbor:"]

    output = ["results/SA_TSP_GEO.csv", "results/SA_TSP_LOG.csv"]

    for i in range(len(file_names)):
        print("========================================================")

        graph = ReadFile(file_names[i])
        temp = Temperature(graph)
        init_temp = temp.find_initial_temperature()

        print("|>", file_names[i])
        print()

        errors = 0.0
        result_times = []

        print(schemas[0])

        for j in range(repeats[i]):
            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, num_iterations)

            timestamp.start()
            best_solution, best_distance = sa.start("geo", "swap")
            result = timestamp.end()
            result_times.append(result)

            if best_distance != results[i]:
                temp = (best_distance - results[i]) / results[i]
                errors = errors + temp

        error_level = (errors / repeats[i]) * 100
        print("Error rate: ", error_level, "%")
        print()

        save_file = SaveToFile(output[0], file_names[i], schemas[0], repeats[i], num_iterations, init_temp,
                               error_level, result_times)
        save_file.save()

        print(schemas[1])

        errors = 0.0
        result_times = []

        for j in range(repeats[i]):
            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)

            timestamp.start()
            best_solution, best_distance = sa.start("geo", "rotation")
            result = timestamp.end()
            result_times.append(result)

            if best_distance != results[i]:
                temp = (best_distance - results[i]) / results[i]
                errors = errors + temp

        error_level = (errors / repeats[i]) * 100
        print("Error rate: ", error_level, "%")
        print()

        save_file = SaveToFile(output[0], file_names[i], schemas[1], repeats[i], num_iterations, init_temp,
                               error_level, result_times)
        save_file.save()

        print(schemas[2])

        errors = 0.0
        result_times = []

        for j in range(repeats[i]):
            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)

            timestamp.start()
            best_solution, best_distance = sa.start("log", "swap")
            result = timestamp.end()
            result_times.append(result)

            if best_distance != results[i]:
                temp = (best_distance - results[i]) / results[i]
                errors = errors + temp

        error_level = (errors / repeats[i]) * 100
        print("Error rate: ", error_level, "%")
        print()

        save_file = SaveToFile(output[1], file_names[i], schemas[2], repeats[i], num_iterations, init_temp,
                               error_level, result_times)
        save_file.save()

        print(schemas[3])

        errors = 0.0
        result_times = []

        for j in range(repeats[i]):
            sa = SimulatedAnnealing(graph, init_temp, cooling_rate, 10000)

            timestamp.start()
            best_solution, best_distance = sa.start("log", "rotation")
            result = timestamp.end()
            result_times.append(result)

            if best_distance != results[i]:
                temp = (best_distance - results[i]) / results[i]
                errors = errors + temp

        error_level = (errors / repeats[i]) * 100
        print("Error rate: ", error_level, "%")
        print()

        save_file = SaveToFile(output[1], file_names[i], schemas[3], repeats[i], num_iterations, init_temp,
                               error_level, result_times)
        save_file.save()


if __name__ == "__main__":
    main()
