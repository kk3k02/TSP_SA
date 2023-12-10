import csv


class SaveToFile:
    def __init__(self, file_name, search, repeats, cost, path, times):
        self.file_name = file_name
        self.search = search
        self.repeats = repeats
        self.cost = cost
        self.path = path
        self.times = times

    def save(self):
        with open('b&b_TSP_output.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            path_without_quotes = str(self.path).strip('"')
            path_without_spaces = path_without_quotes.replace(' ', '')
            writer.writerow([self.file_name, self.search, self.repeats, self.cost, path_without_spaces])
            writer.writerows([[str(time)] for time in self.times])
