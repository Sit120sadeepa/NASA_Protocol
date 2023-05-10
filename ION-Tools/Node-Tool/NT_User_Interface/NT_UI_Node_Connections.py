#import libraies
from tkinter import ttk
import tkinter as tk
import NT_User_Interface.NT_UI_Main
from NT_User_Interface.NT_UI_Error import ErrorGUI
from NT_Node.NT_Node import *
from NT_User_Interface.NT_UI_UpdateWindow import UpdateWindowLocation


#Define a function to close the window with confirmation window
def ConnectNodeGui(windowLocation,nodes,focusNode):
    #Create Higher level Window
    connectNodeWindow = tk.Toplevel()

    #Configure Window
    connectNodeWindow.title('Connect Node')
    connectNodeWindow.windowLocation = windowLocation
    connectNodeWindow.geometry("300x80"+"+"+str(connectNodeWindow.windowLocation[0])+"+"+str(connectNodeWindow.windowLocation[1]))

    windowMessage = tk.Label(connectNodeWindow,text = "Choose Node to connect")
    windowMessage.pack()

    nodeList = []
    for node in nodes:
        if(node.name == focusNode.name):
            None
        nodeList.append(node.name)

    connectedNodeList = []
    connectedNodeList.append(focusNode.name)
    for node in focusNode.connectedNodes:
        if(node.name == focusNode.name):
            None
        connectedNodeList.append(node.name)
        

    uniqueNodes = [x for x in nodeList if x not in connectedNodeList]

    connectNodeWindow.combo = ttk.Combobox(connectNodeWindow,state="readonly",values = uniqueNodes)
    connectNodeWindow.combo.pack()

    def CheckIfNullEntry():
        selectedNode = connectNodeWindow.combo.get()
        found = False
        for node in nodes:
            if(node.name == selectedNode):
                found = True
                focusNode.connectedNodes.append(node)
                node.connectedNodes.append(focusNode)
                UpdateWindowLocation(connectNodeWindow)
                connectNodeWindow.destroy()
                ChangeNodeConnectionsGui(windowLocation,nodes,focusNode)               
                break
        if(not found):
            ErrorGUI(UpdateWindowLocation(connectNodeWindow),"No Node Selected")

    connectButton = tk.Button(connectNodeWindow, width=20 ,text="Connect", command=lambda:CheckIfNullEntry())
    connectButton.pack(side=tk.LEFT)
    cancelButton = tk.Button(connectNodeWindow, width=20 ,text="Cancel", command=lambda:(UpdateWindowLocation(connectNodeWindow),
                                                                                         ChangeNodeConnectionsGui(connectNodeWindow.windowLocation,nodes,focusNode),
                                                                                         connectNodeWindow.destroy()))
    cancelButton.pack(side=tk.LEFT)

#Define a function to close the window with confirmation window
def DisconnectNodeGui(windowLocation,nodes,focusNode):
    #Create Higher level Window

    disconnectNodeWindow = tk.Toplevel()

    #Configure Window
    disconnectNodeWindow.title('Disconnect Node')
    disconnectNodeWindow.windowLocation = windowLocation
    disconnectNodeWindow.geometry("300x80"+"+"+str(disconnectNodeWindow.windowLocation[0])+"+"+str(disconnectNodeWindow.windowLocation[1]))


    windowMessage = tk.Label(disconnectNodeWindow,text = "Choose Node to disconnect")
    windowMessage.pack()

    nodeList = []
    for node in focusNode.connectedNodes:
        if(node.name == focusNode.name):
            None
        nodeList.append(node.name)

    disconnectNodeWindow.combo = ttk.Combobox(disconnectNodeWindow,state="readonly",values = nodeList)
    disconnectNodeWindow.combo.pack()

    def CheckIfNullEntry():
        selectedNode = disconnectNodeWindow.combo.get()
        found = False
        for node in nodes:
            if(node.name == selectedNode):
                found = True
                focusNode.connectedNodes.remove(node)
                node.connectedNodes.remove(focusNode)
                UpdateWindowLocation(disconnectNodeWindow)
                disconnectNodeWindow.destroy()
                ChangeNodeConnectionsGui(windowLocation,nodes,focusNode)               
                break
        if(not found):
                ErrorGUI(UpdateWindowLocation(disconnectNodeWindow),"No Node Selected")

    disconnectButton = tk.Button(disconnectNodeWindow, width=20 ,text="Disconnect", command=lambda:CheckIfNullEntry())
    disconnectButton.pack(side=tk.LEFT)
    cancelButton = tk.Button(disconnectNodeWindow, width=20 ,text="Cancel", command=lambda:(UpdateWindowLocation(disconnectNodeWindow),                                                                                       
                                                                                        NT_User_Interface.NT_UI_Main.MainGUI(disconnectNodeWindow.windowLocation,nodes),
                                                                                        disconnectNodeWindow.destroy()))
    cancelButton.pack(side=tk.LEFT)
    

#Define a function to close the window with confirmation window
def ChangeNodeConnectionsGui(windowLocation,nodes,focusNode):
    #Create Higher level Window
    UI = tk.Toplevel()

    #Configure Window
    UI.title('Modify Node connections')
    UI.windowLocation = windowLocation
    UI.geometry("+"+str(UI.windowLocation[0])+"+"+str(UI.windowLocation[1]))

    connectedNodeList = []
    for node in focusNode.connectedNodes:
        connectedNodeList.append(node.name)

    #Node Name Input Section
    totalColums = 3

    UI.windowMessage = tk.Label(UI,text = "Chosen Node")
    UI.windowMessage.grid(row = 0, column = 0, columnspan = totalColums, pady = 2)
    UI.windowMessage = tk.Label(UI,text = focusNode.name)
    UI.windowMessage.grid(row = 1, column = 0, columnspan = totalColums, pady = 2)

    UI.windowMessage3 = tk.Label(UI,text = "Connected Nodes")
    UI.windowMessage3.grid(row = 2, column = 0, columnspan = totalColums, pady = 2)

    UI.windowMessage4 = tk.Label(UI,text = str(connectedNodeList))
    UI.windowMessage4.grid(row = 3, column = 0, columnspan = totalColums, pady = 2)

    UI.Addbutton = tk.Button(UI, width=20 ,text="Connect a node", command=lambda:(UpdateWindowLocation(UI),                                                            
                                                                                ConnectNodeGui(UI.windowLocation,nodes,focusNode),
                                                                                UI.destroy()))
    UI.Addbutton.grid(row = 4, column = 0, pady = 2)
    UI.Removebutton = tk.Button(UI, width=20 ,text="Disconnect a node", command=lambda:(UpdateWindowLocation(UI),                                                                                 
                                                                                 DisconnectNodeGui(UI.windowLocation,nodes,focusNode),
                                                                                 UI.destroy()))
    UI.Removebutton.grid(row = 4, column = 1, pady = 2)
    UI.cancelButton = tk.Button(UI, width=20 ,text="Back", command=lambda:(UpdateWindowLocation(UI),                                                                             
                                                                             NT_User_Interface.NT_UI_Main.MainGUI(UI.windowLocation,nodes),
                                                                             UI.destroy()))
    UI.cancelButton.grid(row = 4, column = 2, pady = 2)


#Define a function to close the window with confirmation window
def NodeConnectionsGui(windowLocation,nodes):

    #Create Higher level Window
    UI = tk.Toplevel()


    #Configure Window
    UI.title('Select Node')
    UI.windowLocation = windowLocation
    UI.geometry("300x80"+"+"+str(UI.windowLocation[0])+"+"+str(UI.windowLocation[1]))


    UI.windowMessage = tk.Label(UI,text = "Choose a node to change")
    UI.windowMessage.pack()

    nodeList = []
    for node in nodes:
        nodeList.append(node.name)

    UI.combo = ttk.Combobox(UI,state="readonly",values = nodeList)
    UI.combo.pack()

    def CheckIfNullEntry(UI,windowLocation,nodes):
        selectedNode = UI.combo.get()
        found = False
        for node in nodes:
            if(node.name == selectedNode):
                found = True
                #pass through Target Node
                ChangeNodeConnectionsGui(UpdateWindowLocation(UI),nodes,node)
                UI.destroy()
                break
        if(not found):
            ErrorGUI(UpdateWindowLocation(UI),"No Node Selected")

    configureButton = tk.Button(UI, width=20 ,text="Select", command=lambda:CheckIfNullEntry(UI,windowLocation,nodes))
    configureButton.pack(side=tk.LEFT)

    cancelButton = tk.Button(UI, width=20 ,text="Cancel", command=lambda:(UpdateWindowLocation(UI),
                                                                          NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes),
                                                                          UI.destroy()))
    cancelButton.pack(side=tk.LEFT)