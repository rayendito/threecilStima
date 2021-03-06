
from Graph import Graph, Simpul
from Prioqueue import PrioQueue, Path

# Mengecek apakah pada suatu path sudah terdapatt simpul yang dicari
def dikunjungi(path, indexDicari):
    for item in path.getArraySimps():
        if(item.getIndex() == indexDicari):
            return True
    return False

# Mengambil simpul berdasarkan index
def getSimpulFromIndex(index, ArraySimps):
    for item in ArraySimps:
        if(item.getIndex() == index):
            return item
    return -1 # kalau ga ditemukan

def getSimpulbyName(Name, ArraySimps):
    for item in ArraySimps:
        if(item.getName() == Name):
            return item
    return -1 # error code

# Find path using A* algorithm
# Source dan destination bertipe Simpul
# Mengembalikan array 1 elemeen bertipe Path
def findPath(source, destination, Graf):
    FinalPath = []
    # inisialisasi sebuah priority queue
    Queue = PrioQueue()
    jalur = Path([source], 0, Graf.getDistHaversine(source, destination))
    Queue.enqueue(jalur)
    found = False # Untuk mendeteksi apakah sudah menemukan Simpul tujuan
    i = 1
    while(not Queue.isEmpty()):
        jalur = Queue.dequeue()
        IndexLast = len(jalur.getArraySimps()) -1
        lastVertex = jalur.getArraySimps()[IndexLast]
        index = lastVertex.getIndex()
        arraySimpulBaru = []

        for i in range(len(Graf.simps)):
            # print(str(i) + "-------")
            if(Graf.adjMat[index][i] > 0 and not dikunjungi(jalur, i)):
                # Kumpulkan jalur sebelumnya + simpul baru yang dibangkitkan
                arraySimpulBaru = jalur.getArraySimps()
                newSimpul = getSimpulFromIndex(i, Graf.getSimps())
                arraySimpulBaru.append(newSimpul)

                # Siapkan atribut new Path
                newCost = jalur.getCostSoFar()+Graf.adjMat[index][i] # g(n)
                sld = Graf.getDistHaversine(newSimpul, destination) #h(n)
                newPath = Path(arraySimpulBaru,newCost, newCost+sld)
                Queue.enqueue(newPath)
                # Cek apakah sudah sampai ke destination
                if(newSimpul.getIndex() == destination.getIndex()):
                    found = True
                    if(len(FinalPath) == 0):
                        FinalPath.append(newPath)
                    else:
                        if(newPath.getBobot() > FinalPath[0].getBobot()):
                            FinalPath[0] = newPath
                
                # Hapus simpul baru untuk disiapkan menjadi simpul yang lain
                arraySimpulBaru.pop()
        # Sudah tidak ada jalur yang lebih pendek dari final path sekarang
        if(found and (Queue.isEmpty() or FinalPath[0].getBobot() <= Queue.Top().getBobot())):
            FinalPath[0].printPath()
            return FinalPath
    # Jika tidak ditemukan, FinalPath kosong
    return FinalPath