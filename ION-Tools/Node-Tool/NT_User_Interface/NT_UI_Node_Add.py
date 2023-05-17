#import libraies
import tkinter as tk

#Import Scripts from directory
import NT_User_Interface.NT_UI_Main
from NT_User_Interface.NT_UI_Error import ErrorGUI
from NT_Node.NT_Node import *
from NT_User_Interface.NT_UI_UpdateWindow import UpdateWindowLocation


#User interface for creating new nodes
def AddNodeGui(windowLocation,nodes):

    UI = tk.Toplevel()

    #Configure Window
    UI.title('Add Node')
    UI.windowLocation = windowLocation
    UI.geometry("+"+str(UI.windowLocation[0])+"+"+str(UI.windowLocation[1]))

    #Node Name Input Section
    totalColums = 7

    UI.message = tk.Label(UI, text="Enter Node Name (Max 32 char)")
    UI.message.grid(row = 0, column = 0, columnspan = totalColums, pady = 2)

    UI.nodeNameEntry = tk.Entry(UI, width=20)
    UI.nodeNameEntry.grid(row = 1, column = 0, columnspan = totalColums, pady = 2)

    input_size = 10

    #Ip address Input Section
    UI.IPinputMessage = tk.Label(UI, text="IP address for node")
    UI.IPinputMessage.grid(row = 3, column = 0, columnspan = totalColums, pady = 2)

    #oct 1 input
    UI.IPaddressBit1 = tk.Entry(UI, width=input_size)
    UI.IPaddressBit1.grid(row = 4, column = 0,  pady = 2)

    UI.dot1 = tk.Label(UI,text=".")
    UI.dot1.grid(row = 4, column = 1,  pady = 2)
    #oct 2 input
    UI.IPaddressBit2 = tk.Entry(UI, width=input_size)
    UI.IPaddressBit2.grid(row = 4, column = 2,  pady = 2)

    UI.dot2 = tk.Label(UI,text=".")
    UI.dot2.grid(row = 4, column = 3,  pady = 2)
    #oct 3 input
    UI.IPaddressBit3 = tk.Entry(UI, width=input_size)
    UI.IPaddressBit3.grid(row = 4, column = 4,  pady = 2)

    UI.dot3 = tk.Label(UI,text=".")
    UI.dot3.grid(row = 4, column = 5,  pady = 2)
    #oct 4 input
    UI.IPaddressBit4 = tk.Entry(UI, width=input_size)
    UI.IPaddressBit4.grid(row = 4, column = 6,  pady = 2)



    def CreateNode(UI,nodes):
        if (inputValdation(UI,nodes)):
            node = NodeConstructor()
            node.name = UI.nodeNameEntry.get()
            node.IPAddress = [UI.IPaddressBit1.get(),UI.IPaddressBit2.get(),UI.IPaddressBit3.get(),UI.IPaddressBit4.get()]
            AddNode(nodes,node)
            UpdateWindowLocation(UI)
            UI.destroy()
            NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)

    UI.confirmbutton = tk.Button(UI, width=16, text="Create Node", command=lambda:CreateNode(UI,nodes))
    UI.confirmbutton.grid(row = 6, column = 0, columnspan = 3, pady = 2)
    UI.cancelButton = tk.Button(UI, width=16 ,text="Cancel", command=lambda:(UpdateWindowLocation(UI),
                                                                             UI.destroy(),
                                                                             NT_User_Interface.NT_UI_Main.MainGUI(windowLocation,nodes)))
    UI.cancelButton.grid(row = 6, column = 4, columnspan = 3, pady = 2)
 