import re

class Graph:
    g = []
    vertices = 0

    def __init__(self, filename):
        self.loadFromFile(filename)

    def loadFromFile(self, filename):
        self.g = []
        file = open(filename,"r")


        lastThreeCharacters = filename[-3] + filename[-2] + filename[-1]


        if lastThreeCharacters == "xml":
            line = file.readline()

            while(line!="  <graph>\n"): #skip to edge declaration part of file
                line = file.readline()

            #inserts distance values for graph
            while(line!="  </graph>\n"):
                distances = []  #array of distances for one vertex
                # inserts distance values for one vertex
                while(line!="    </vertex>\n"):
                    #checks if line has declaration part
                    nodeNumber = 0

                    if(line[6:17] == "<edge cost="):
                        num = re.findall(r'\d+', line[41:44])
                        currentNumber = int(num[0])

                        if currentNumber != nodeNumber:
                            distances.append((9.99)*(10**100))
                            nodeNumber = currentNumber

                        costBase = float(line[18:35])   #edge cost - base
                        costPower = float(line[37:39])  #edge cost - power


                        #cost is written in scientific notation
                        cost = costBase * (10**costPower)
                        distances.append(cost)
                        nodeNumber = nodeNumber + 1
                        print(currentNumber, " : ", nodeNumber)

                    line = file.readline()

                #append row to matrix
                self.g.append(distances)

                #skip to next vertex declaration
                line = file.readline()

        elif(lastThreeCharacters == "txt"):
            print("txt")
            self.vertices = int(file.readline())

            for i in range(self.vertices):
                distance = [int(x) for x in file.readline().split()]
                self.g.append(distance)

        self.vertices = len(self.g)

        # Zamykanie pliku
        file.close()