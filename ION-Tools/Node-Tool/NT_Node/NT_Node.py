from NT_User_Interface.NT_UI_Error import ErrorGUI
from NT_User_Interface.NT_UI_UpdateWindow import UpdateWindowLocation
# declare constants 
NAMECHARLIMIT = 32


#Universal definitions of node functions
class node():
    def __init__(self):
        self.name = ""
        self.IPAddress = []
        self.connectedNodes = []

def AddNode(nodes,node):
    nodes.append(node)

def NodeConstructor():
        return node()

def RemoveNode(nodes,nodeName):
    for node in nodes:
        if(node.name==nodeName):
            for connectedNode in node.connectedNodes:
                connectedNode.connectedNodes.remove(node)
            nodes.remove(node)
            break

#input validation for IP address input for node
def inputValdation(UI,nodes):
    ipList = []
    for node in nodes:
        ipList.append(node.IPAddress)

    invalid = False
    nameInput = UI.nodeNameEntry.get()
    if(len(nameInput)==0):
            ErrorGUI(UpdateWindowLocation(UI),"No name entered")
            return False

    for node in nodes:
        if(node.name==nameInput):
            ErrorGUI(UpdateWindowLocation(UI),"Node "+nameInput+" Allready Exists")
            return False


    if(len(nameInput)>NAMECHARLIMIT):
        ErrorGUI(UpdateWindowLocation(UI),"Character limit Exceeded\n Maximum allowed characters : "+str(NAMECHARLIMIT))
        return False
        
    octets = [UI.IPaddressBit1.get(),UI.IPaddressBit2.get(),UI.IPaddressBit3.get(),UI.IPaddressBit4.get()]

    for octet in octets:
        if(len(octet)==0):
            ErrorGUI(UpdateWindowLocation(UI),"No IP address entered")
            invalid = True
            break
        elif(not octet.isnumeric()):
            ErrorGUI(UpdateWindowLocation(UI),"Octets must only contain integers")
            invalid = True
            break
        elif(int(octet)>255 or int(octet)<0):
            ErrorGUI(UpdateWindowLocation(UI),"One or more octets are out of range\n Range : 0-255")
            invalid = True
            break
    for IP in ipList:
        if(IP == octets):
            ErrorGUI(UpdateWindowLocation(UI),"Duplicate IP on network")
            invalid = True
            break

    if(invalid == True):
        return False
    else:
        return True