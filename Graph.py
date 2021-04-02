class Simpul:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def getName(self):
        return self.name
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

class Graph:
    def __init__(self, path):
        #inisialisasi atribut
        self.simps = []
        self.adjMat = []

        #baca file
        file = open(path, "r")
        lines = file.readlines()
        ens = int(lines[0])
        for i in range(1,ens+1):
            info = lines[i].split()
            self.simps.append(Simpul(info[0], float(info[1]), float(info[2])))
        
        for i in range(ens+1,len(lines)):
            a_list = lines[i].split()
            map_object = map(int, a_list)
            self.adjMat.append(list(map_object))
    
    def getSimps(self):
        return self.simps
    
    def getAdjMat(self):
        return self.adjMat

    def printSimps(self):
        for i in self.simps:
            print(i.getName() + str(i.getX()) + str(i.getY()))

    def printAdjMat(self):
        for i in self.adjMat:
            print(i)

a = Graph("sample.txt")
a.printAdjMat()
a.printSimps()