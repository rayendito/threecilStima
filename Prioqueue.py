class Path:
    def __init__(self, arraySimps, Bobot):
        self.arraySimps = arraySimps
        self.Bobot = Bobot
    
    def getArraySimps(self):
        return self.arraySimps

    def getBobot(self):
        return self.Bobot

    def printPath(self):
        print("List Path", end=" : ")
        for i in self.arraySimps:
            print(i, end=" ")
        print("; Bobot", self.Bobot)

class PrioQueue:
    def __init__(self):
        self.Queue = [] # Berisi tipe Path

    def enqueue(self, Path):
        if(len(self.Queue) == 0):
            self.Queue.append(Path)
        else:
            i = 0
            while(i < len(self.Queue) and Path.Bobot > self.Queue[i].Bobot):
                i += 1
            if(i == len(self.Queue)):
                self.Queue.append(Path)
            else:
                self.Queue.insert(i, Path)
    

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
path1 = Path(["A", "B"], 10)
path2 = Path(["C", "D"], 20)
path3 = Path(["E", "F"], 5)
path4 = Path(["G", "H"], 17)

# Construct queue
Queue = PrioQueue()
# Test enqueue
Queue.enqueue(path1)
Queue.enqueue(path2)
Queue.enqueue(path3)
Queue.enqueue(path4)
Queue.printQueue()
# Delete queue
while(not Queue.isEmpty()):
    first = Queue.dequeue()

