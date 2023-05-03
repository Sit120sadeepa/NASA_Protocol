#import libraies
import tkinter as tk
import igraph as ig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from NT_Graph_Generation.NT_GraphGen import GenerateGraph
from NT_File_Output.NT_Export_RC import GenerateRCFiles


networkMap = ig.Graph(directed=False)
#Create Initial vertice - Minumum of 1 required
networkMap.add_vertices(1)


#Define a function to close the window with confirmation window
def DrawGraph(UI,nodes):
    #Create Higher level Window
    graphWindow = tk.Toplevel()
    graphWindow.title('Network Graph')
    graphMessage1 = tk.Label(graphWindow, text="Diagram of current network configuration")
    graphMessage1.pack()

    fig = GenerateGraph(nodes)
    graph = FigureCanvasTkAgg(fig, graphWindow)
    graph.get_tk_widget().pack(fill=tk.BOTH)
    saveButton = tk.Button(graphWindow, width=50 ,text="Generate RC files", command=lambda:GenerateRCFiles(nodes))
    saveButton.pack(side=tk.LEFT)
    closeButton = tk.Button(graphWindow, width=50 ,text="Close Graph", command=lambda:graphWindow.destroy())
    closeButton.pack(side=tk.LEFT)