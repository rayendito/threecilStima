
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
            print("Pencarian selesai, telah ditemukan")
            return FinalPath
    # Jika tidak ditemukan, FinalPath kosong
    return FinalPath

graf = Graph("Alunalun.txt")
# graf.printSimps()
# allSimpul = graf.getSimps()

''' Ngetes Jarak '''
# print("Jarak antara : " + str(allSimpul[0].getName()) + " " + str(allSimpul[1].getName()))
# print(graf.getDistHaversine(allSimpul[0], allSimpul[1]))

# print("================ TC 1 ===========================")
# path = findPath(graf.getSimps()[0], graf.getSimps()[4], graf)
# path[0].printPath()
# path = findPath(graf.getSimps()[5], graf.getSimps()[3], graf)
# print("================ TC 2 ===========================")
# path[0].printPath()
# path = findPath(graf.getSimps()[3], graf.getSimps()[7], graf)
# print("================ TC 3 ===========================")
# path[0].printPath()
# path = findPath(graf.getSimps()[9], graf.getSimps()[2], graf)
# print("================ TC 4 ===========================")
# path[0].printPath()


def createAllMarker(arraySimpul, m): # f= figure group, m = map
    f=folium.FeatureGroup("Simpul")
    for simpul in arraySimpul:
        folium.Marker(location=[simpul.getX(), simpul.getY()],popup=simpul.getName(),
                      icon = folium.Icon(color="green"),
                      tooltip=simpul.getName()).add_to(f)
    f.add_to(m)

# Draw All line
def drawPathfromGraph(listSimpul, adjMat, Map):
    f1=folium.FeatureGroup("All path")
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(i<j and mat[i][j] != 0):
                garis = [[listSimpul[i].getX(), listSimpul[i].getY()], [listSimpul[j].getX(), listSimpul[j].getY()]]
                line_1=folium.vector_layers.PolyLine(garis,popup="Jarak : " + str(adjMat[i][j]) + " km",
                                                     tooltip=listSimpul[i].getName() + " - " + listSimpul[j].getName(),
                                                     color='#4878b8',weight=7.5).add_to(f1)
    f1.add_to(Map)


# Draw final path
def drawFinalPath(Path, Map, arraySimpFromGraf, adjMat):
    f=folium.FeatureGroup("Final Path")
    for i in range (len(Path.getArraySimps())-1):
        indexA = Path.getArraySimps()[i].getIndex()
        simpA = getSimpulFromIndex(indexA, arraySimpFromGraf)
        indexB = Path.getArraySimps()[i+1].getIndex()
        simpB = getSimpulFromIndex(indexB, arraySimpFromGraf)
        garis = [[simpA.getX(), simpA.getY()], [simpB.getX(), simpB.getY()]]
        line_1=folium.vector_layers.PolyLine(garis, 
                                             popup = "Jarak : " + str(adjMat[indexA][indexB]) + " km",
                                             tooltip=simpA.getName() + " - " + simpB.getName(),
                                             color='#cf1b1b',weight=7.5).add_to(f)
    f.add_to(Map)
    
    # Tambahkan marker untuk path final,ntar aja di main deng
    # createAllMarker(Path.getArraySimps(), Map, "orange", "labelGroup")
    

''' TEST ''' 
# #print jalan
# from Graph import Graph, Simpul
# from Prioqueue import PrioQueue, Path
# import main as mn
# a = Graph("buahbatu.txt")
# listSimpul = a.getSimps()
# adjmat = a.getAdjMat()
# p = Path([listSimpul[0], listSimpul[5], listSimpul[4]], 100, 50) # Testing

# m=folium.Map(location=[listSimpul[0].getX(), listSimpul[0].getY()], zoom_start=15)
# createAllMarker(listSimpul, m, "cadetblue", "All Vertex")
# drawPathfromGraph(listSimpul, adjmat, m)
# drawFinalPath(p, m, listSimpul, adjmat)
# folium.LayerControl().add_to(m)
# m