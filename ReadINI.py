class ReadINI:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        file_names = []
        repeats = []
        with open(self.file_path, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) >= 3:
                    file_name = parts[0]
                    repeat = int(parts[1])
                    file_names.append(file_name)
                    repeats.append(repeat)
        return file_names, repeats
