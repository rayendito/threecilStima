import Graph


class Path:
    # CostsoFar = jarak sebenarnya
    # bobot = jarak sebenarnya + sld
    def __init__(self, arraySimpul, costSoFar, Bobot):
        self.arraySimps = []
        for item in arraySimpul:
            self.arraySimps.append(item)
        self.Bobot = Bobot
        self.costSoFar = costSoFar
    
    def insertNewSimp(self, newSimpul):
        self.arraySimps.append(newSimpul)

    def getCostSoFar(self):
        return self.costSoFar

    def getArraySimps(self):
        return self.arraySimps

    def getBobot(self):
        return self.Bobot

    def printPath(self):
        print("Jalur : ")
        for i in range (len(self.arraySimps)):
            if(i == len(self.arraySimps)-1):
                 print(self.arraySimps[i].getName())
            else:
                print(self.arraySimps[i].getName(), end=" → ")
        print("Jarak tempuh : ", round(self.Bobot*1000,2), "m")

class PrioQueue:
    def __init__(self):
        self.Queue = [] # Berisi tipe Path

    def enqueue(self, Path):
        i = 0
        while(i < len(self.Queue) and Path.Bobot > self.Queue[i].Bobot):
            i += 1
        if(i == len(self.Queue)):
            self.Queue.append(Path)
        else:
            self.Queue.insert(i, Path)
    
    def Top(self):
        return self.Queue[0]

    def isEmpty(self):
        return (len(self.Queue) == 0)
    
    def dequeue(self):
        if(self.isEmpty()):
            return 404 #error code
        else:
            return self.Queue.pop(0)
    
    def printQueue(self):
        if(self.isEmpty()):
            print("Priority queue is empty")
        else:
            for jalur in self.Queue:
                jalur.printPath()