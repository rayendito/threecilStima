from math import radians, cos, sin, asin, sqrt

class Simpul:
    def __init__(self, name, x, y, index):
        self.name = name
        self.x = x
        self.y = y
        self.index = index

    def getName(self):
        return self.name
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getIndex(self):
        return self.index

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
            self.simps.append(Simpul(info[0], float(info[1]), float(info[2]), i-1))
        
        for i in range(ens+1,len(lines)):
            a_list = lines[i].split()
            map_object = map(int, a_list)
            self.adjMat.append(list(map_object))

        for i in range(ens):
            for j in range(ens):
                if(i<j and self.adjMat[i][j] != 0):
                    hv = self.getDistHaversine(self.simps[i], self.simps[j])
                    self.adjMat[i][j] = hv
                    self.adjMat[j][i] = hv
                    
    
    def getDistHaversine(self, pointA, pointB):
        #jadikan dalam satuan radian
        loA = radians(pointA.getY())
        loB = radians(pointB.getY())
        laA = radians(pointA.getX())
        laB = radians(pointB.getX())

        #rumus haversine
        slon = loB - loA 
        slat = laB - laA
        a = sin(slat / 2)**2 + cos(laA) * cos(laB) * sin(slon / 2)**2
        
        #return
        return(2 * asin(sqrt(a)) * 6371)


    def getSimps(self):
        return self.simps
    
    def getAdjMat(self):
        return self.adjMat

    def printSimps(self):
        for i in self.simps:
            print(i.getName() + " " + str(i.getX()) + " " + str(i.getY()) + " Index : " + str(i.getIndex()))

    def printAdjMat(self):
        for i in self.adjMat:
            print(i)

# a = Graph("Alunalun.txt")
# a.printAdjMat()
# a.printSimps()