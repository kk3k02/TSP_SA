from ReadINI import ReadINI
from ReadFile import ReadFile
from SimulatedAnnealing import SimulatedAnnealing

def main():
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

if __name__ == "__main__":
    main()