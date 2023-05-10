#import libraies
from tkinter import ttk
import tkinter as tk

#Import Scripts from directory
import NT_User_Interface.NT_UI_Main
from NT_Node.NT_Node import *
from NT_User_Interface.NT_UI_UpdateWindow import UpdateWindowLocation


#Define a function to close the window with confirmation window
def RemoveNodeGui(windowLocation,nodes):
    #Create Higher level Window
    removeNodeWindow = tk.Toplevel()

    #Configure Window
    removeNodeWindow.geometry("300x80"+"+"+str(windowLocation[0])+"+"+str(windowLocation[1]))
    removeNodeWindow.windowLocation = windowLocation
    removeNodeWindow.title('Remove Node')

    windowMessage = tk.Label(removeNodeWindow,text = "Choose Node to remove")
    windowMessage.pack()

    nodeList = []
    for node in nodes:
        nodeList.append(node.name)

    combo = ttk.Combobox(removeNodeWindow,state="readonly",values = nodeList)
    combo.pack()

    deleteButton = tk.Button(removeNodeWindow, width=20 ,text="Delete", command=lambda:(RemoveNode(nodes,combo.get()),
                                                                                        UpdateWindowLocation(removeNodeWindow),
                                                                                        removeNodeWindow.destroy(),
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(removeNodeWindow.windowLocation,nodes)))
    deleteButton.pack(side=tk.LEFT)
    cancelButton = tk.Button(removeNodeWindow, width=20 ,text="Cancel", command=lambda:(UpdateWindowLocation(removeNodeWindow),
                                                                                        removeNodeWindow.destroy(),
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(removeNodeWindow.windowLocation,nodes)))
    cancelButton.pack(side=tk.LEFT)