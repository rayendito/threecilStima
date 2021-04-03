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
        print("Path : ")
        for i in range (len(self.arraySimps)):
            if(i == len(self.arraySimps)-1):
                 print(self.arraySimps[i].getName())
            else:
                print(self.arraySimps[i].getName(), end=" -> ")
        print("Bobot", self.Bobot)

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


''' TESTING '''
# Construct path

# s1 = Graph.Simpul("DayangSumbi", 0, 12)
# s2 = Graph.Simpul("TubagusIsmail", 2, 40)
# s3 = Graph.Simpul("Siliwangi", 3, 26)
# s4 = Graph.Simpul("Tegallega", 7, 11)
# s5 = Graph.Simpul("Bubat", 31, 5)

# path1 = Path([s1,s2], 10)
# path2 = Path([s3], 20)
# path3 = Path([s4], 5)
# path4 = Path([s5], 17)

# # Construct queue
# Queue = PrioQueue()
# # Test enqueue
# Queue.enqueue(path1)
# Queue.enqueue(path2)
# Queue.enqueue(path3)
# Queue.enqueue(path4)
# # Queue.printQueue()
# # Delete queue
# while(not Queue.isEmpty()):
#     first = Queue.dequeue()
#     # print(first.arraySimps[0].getName())
#     first.printPath()

# Queue.printQueue()


# s1 = Simpul("DayangSumbi", 0, 12,0)
# s2 = Simpul("TubagusIsmail", 2, 40,1)
# s3 = Simpul("Siliwangi", 3, 26,2)
# s4 = Simpul("Tegallega", 7, 11,3)
# s5 = Simpul("Bubat", 31, 5,4)
# q = PrioQueue()
# p = Path([s1,s2], 5, 10)
# s = Path([s3,s4], 10, 20)
# q.enqueue(p)
# q.enqueue(s)
# q.dequeue()
# print(q.Top().getBobot())
# q.printQueue()
# graf.printAdjMat()