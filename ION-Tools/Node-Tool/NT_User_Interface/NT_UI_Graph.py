# Import libraries
import sys
import networkx as nx
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from NT_Graph_Generation.NT_GraphGen import GenerateGraph
from NT_File_Output.NT_Export_RC import GenerateRCFiles

# Create an empty networkx graph
networkMap = nx.Graph()

# Add an initial vertex (minimum of 1 required)
networkMap.add_node(0)

# Define a function to close the window with a confirmation window
def DrawGraph(UI, nodes):
    # Create a higher-level window
    graphWindow = tk.Toplevel()
    graphWindow.title('Network Graph')
    graphMessage1 = tk.Label(graphWindow, text="Diagram of the current network configuration")
    graphMessage1.pack()

    fig = GenerateGraph(nodes)
    graph = FigureCanvasTkAgg(fig, graphWindow)
    graph.get_tk_widget().pack(fill=tk.BOTH)
    saveButton = tk.Button(graphWindow, width=50, text="Generate RC files", command=lambda: GenerateRCFiles(nodes))
    saveButton.pack(side=tk.LEFT)
    closeButton = tk.Button(graphWindow, width=50, text="Close Graph", command=lambda: graphWindow.destroy())
    closeButton.pack(side=tk.LEFT)