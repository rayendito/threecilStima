
from Graph import Graph, Simpul
from Prioqueue import PrioQueue, Path
# from modules.Prioqueue import Path, PrioQueue

# print("a")
# a = Simpul("Halo",2,3)
# print(a.getName())

# a.printAdjMat()
# a.printSimps()

def dikunjungi(path, indexDicari):
    for item in path.getArraySimps():
        if(item.getIndex() == indexDicari):
            return True
    return False

def getSimpulFromIndex(index, ArraySimps):
    for item in ArraySimps:
        if(item.getIndex() == index):
            return item
    return -1 # kalau ga ditemukan

# Find path using A* algorithm
# Source dan destination bertipe SImpul

# Mengembalikan array 1 elemeen bertipe Path
def findPath(source, destination, Graf):
    FinalPath = []
    # inisialisasi sebuah priority queue
    Queue = PrioQueue()
    jalur = Path([source], 0, Graf.getDistHaversine(source, destination))
    Queue.enqueue(jalur)
    jalur.printPath()
    found = False # Untuk mendeteksi apakah sudah menemukan Simpul tujuan
    i = 1
    while(not Queue.isEmpty()):
        jalur = Queue.dequeue()
        IndexLast = len(jalur.getArraySimps()) -1
        lastVertex = jalur.getArraySimps()[IndexLast]
        index = lastVertex.getIndex()
        listSimpul = jalur.getArraySimps()
        # print("============")
        # print(lastVertex.getName())
        # print("============")
        # Queue.printQueue()
        # print("#################")


        print("Yang diproses : ", lastVertex.getName())
        for i in range(len(Graf.simps)):
            # print(str(i) + "-------")
            if(Graf.adjMat[index][i] > 0 and not dikunjungi(jalur, i)):
                # Kumpulkan jalur sebelumnya + simpul baru yang dibangkitkan
                arraySimpulBaru = jalur.getArraySimps()
                newSimpul = getSimpulFromIndex(i, Graf.getSimps())
                # print(newSimpul.getName())
                arraySimpulBaru.append(newSimpul)

                # Siapkan atribut new Path
                newCost = jalur.getCostSoFar()+Graf.adjMat[index][i] # g(n)
                sld = Graf.getDistHaversine(newSimpul, destination) #h(n)
                newPath = Path(arraySimpulBaru,newCost, newCost+sld)
                newPath.printPath()
                Queue.enqueue(newPath)
                # Cek apakah sudah sampai ke destination
                if(newSimpul.getIndex() == destination.getIndex()):
                    found = True
                    if(len(FinalPath) == 0):
                        FinalPath.append(newPath)
                    else:
                        if(newPath.getBobot() > FinalPath[0].getBobot()):
                            FinalPath[0] = newPath
        # Sudah tidak ada jalur yang lebih pendek dari final path sekarang
        if(found and (Queue.isEmpty() or FinalPath[0].getBobot() <= Queue.Top().getBobot())):
            print("Pencarian selesai, telah ditemukan")
            return FinalPath
        
        Queue.printQueue()
        print()
        print()
        #jalur.printPath()
    # Jika tidak ditemukan, FInalPath kosong
    return FinalPath

graf = Graph("Alunalun.txt")
# graf.printSimps()
# allSimpul = graf.getSimps()

''' Ngetes Jarak '''
# print("Jarak antara : " + str(allSimpul[0].getName()) + " " + str(allSimpul[1].getName()))
# print(graf.getDistHaversine(allSimpul[0], allSimpul[1]))

item = getSimpulFromIndex(5, graf.getSimps())


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
graf.printAdjMat()
path = findPath(graf.getSimps()[0], graf.getSimps()[2], graf)


