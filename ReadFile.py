class ReadFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        num_ver = 0
        cost_list = []
        with open(self.file_path, "r") as file:
            num_ver = int(file.readline())
            for i in range(num_ver):
                distance = [int(x) for x in file.readline().split()]
                cost_list.append(distance)
        return cost_list
