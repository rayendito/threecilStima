#untuk map
import folium
from folium import plugins

#untuk rute
from Graph import Graph, Simpul
from Prioqueue import PrioQueue, Path
from function import *

#untuk widget tool
import ipywidgets as widgets

### MARKER AND PATH ROUTE ###
def createAllMarker(arraySimpul, m, warna, labelGroup): # f= figure group, m = map
    f=folium.FeatureGroup(labelGroup)
    for simpul in arraySimpul:
        folium.Marker(location=[simpul.getX(), simpul.getY()],popup=simpul.getName(),
                      icon = folium.Icon(color=warna),
                      tooltip=simpul.getName()).add_to(f)
    f.add_to(m)

# Draw All line
def drawPathfromGraph(listSimpul, adjMat, Map):
    f1=folium.FeatureGroup("All path")
    for i in range(len(adjMat)):
        for j in range(len(adjMat)):
            if(i<j and adjMat[i][j] > 0):
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


### WIDGETS ###
#input box text file
namaFile = widgets.Text(
    value='',
    placeholder='Input file name',
    description='File:',
    disabled=False
)

#dropdown asal
asal = widgets.Dropdown(
    options=['placeholder'],
    value='placeholder',
    description='From :',
    disabled=False
)

#dropdown tujuan
tujuan = widgets.Dropdown(
    options=['placeholder'],
    value='placeholder',
    description='To :',
    disabled=False
)

#go button
go = widgets.Button(
    description='Go',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='' # (FontAwesome names without the `fa-` prefix)
)

#cancel button
cancel = widgets.Button(
    description='Reset',
    disabled=False,
    button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='' # (FontAwesome names without the `fa-` prefix)
)

#findroutebutton
find = widgets.Button(
    description='Find Route',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='' # (FontAwesome names without the `fa-` prefix)
)

#labels
title = widgets.VBox([widgets.Label('GOOGOLMEPZ')]
,layout=widgets.Layout(width='100%', display='flex' ,
align_items='center'))
initial_map = widgets.Label(value="Initial Map")

### GROUPING ###
upfile = [namaFile,go]
whereto = [asal,tujuan,find,cancel]

### OUTPUTS ###
outputFileSelect = widgets.Output()
outputSearch = widgets.Output()
outputCancel = widgets.Output()

### HANDLERS ###
def cuancel(event):
    with outputCancel:
        outputFileSelect.clear_output()
        outputSearch.clear_output()

def searchGo(event):
    with outputSearch:
        a = Graph(namaFile.value)
        listSimpul = a.getSimps()
        adjmat = a.getAdjMat()

        # A* algorithm
        try:
            outputSearch.clear_output()
            #mencari dari asal ke tujuan dengan A*
            p = findPath(getSimpulbyName(asal.value,listSimpul), getSimpulbyName(tujuan.value,listSimpul), a)
            #path hasil adahal p[0]
            finalP = p[0]

            #menggambar alur ke layar
            m=folium.Map(location=[listSimpul[0].getX(), listSimpul[0].getY()], width='100%', height='100%', zoom_start=15.5)
            createAllMarker(listSimpul, m, "cadetblue", "All Vertex")
            drawPathfromGraph(listSimpul, adjmat, m)
            drawFinalPath(finalP, m, listSimpul, adjmat)
            createAllMarker(finalP.getArraySimps(), m, "orange", "Visited")
            folium.LayerControl().add_to(m)
            #Add scroll Zoom toggler left bottom
            plugins.ScrollZoomToggler().add_to(m)
            # Add fullscreen button
            plugins.Fullscreen(position='topright').add_to(m)

            #mencetak map ke layar
            display(m)
        except IndexError:
            #jika asal dan tujuan di tempat yang sama
            print("0 m")

def fileSelect(event):
    with outputFileSelect:
        try:
            #coba loadfile jika file ada
            outputFileSelect.clear_output()
            a = Graph(namaFile.value)
            listSimpul = a.getSimps()
            adjmat = a.getAdjMat()

            #menggambar map awal
            m = folium.Map(location=[listSimpul[0].getX(), listSimpul[0].getY()], width='100%', height='100%', zoom_start=15.5)
            createAllMarker(listSimpul, m, "cadetblue", "All Vertex")
            drawPathfromGraph(listSimpul, adjmat, m)
            #Add scroll Zoom toggler left bottom
            plugins.ScrollZoomToggler().add_to(m)
            # Add fullscreen button
            plugins.Fullscreen(position='topright').add_to(m)

            #set options untuk dropdown
            names = []
            for i in listSimpul:
                names.append(i.getName())
            asal.options = names
            asal.value = names[0]
            tujuan.options = names
            tujuan.value = names[0]

        except FileNotFoundError:
            print("File tidak ditemukan, pastikan nama file benar")
        else:
            #tidak ada error, file fitemukan
            display(widgets.HBox(whereto))
            display(outputSearch)
            display(initial_map)
            display(m)

### ONCLICKS ###
go.on_click(fileSelect)
cancel.on_click(cuancel)
find.on_click(searchGo)

### START ###
start = widgets.HBox(upfile, layout = widgets.Layout(width='100%', justify_content='flex-start'))