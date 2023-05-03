#import libraies
import io

def GenerateRC(primaryNode):

    nodeName = primaryNode.name
    nodeIP = str(primaryNode.IPAddress[0])+"."+str(primaryNode.IPAddress[1])+"."+str(primaryNode.IPAddress[2])+"."+str(primaryNode.IPAddress[3])

    RCFile = []
    #Each new Append is a new line
    #Ion Secadmin Segment
    RCFile.append("## begin ionsecadmin")
    RCFile.append("1")
    RCFile.append("## end ionsecadmin")
    RCFile.append("")
    #Ionadmin Segment
    RCFile.append("## begin ionadmin")
    RCFile.append("1 "+nodeName+ '')
    RCFile.append("s")
    RCFile.append("")
    RCFile.append("m horizon +0")
    RCFile.append("")
    RCFile.append("# Series of 1-hour contacts")
    for node in primaryNode.connectedNodes:
        RCFile.append("a contact +0 +3600 "+nodeName+" "+nodeName+" "+"10000000 1")
        RCFile.append("a contact +0 +3600 "+node.name+" "+nodeName+" "+"10000000 1")
        RCFile.append("a contact +0 +3600 "+nodeName+" "+node.name+" "+"10000000 1")
        RCFile.append("a contact +0 +3600 "+node.name+" "+node.name+" "+"10000000 1")
    RCFile.append("")

    RCFile.append("# Series of 1-hour ranges")
    for node in primaryNode.connectedNodes:
        RCFile.append("a range +0 +3600 "+nodeName+" "+nodeName+"1")
        RCFile.append("a range +0 +3600 "+node.name+" "+nodeName+"1")
        RCFile.append("a range +0 +3600 "+nodeName+" "+node.name+"1")
        RCFile.append("a range +0 +3600 "+node.name+" "+node.name+"1")

    RCFile.append("")
    #define limits
    RCFile.append("m production 10000000")
    RCFile.append("m consumption 10000000")

    RCFile.append("## end ionadmin")
    RCFile.append("")

    #ltpadmin Segment
    RCFile.append("## begin ltpadmin")
    RCFile.append("1 32 ''")
    RCFile.append("")
    RCFile.append("# LTP span for loopback connection")
    # LTP span for loopback connection
    RCFile.append("a span "+nodeName+" 32 32 1400 10000 1 'udplso "+nodeIP+":1113' 300")
    RCFile.append("")
    RCFile.append("s 'udplsi "+nodeIP+":1113'")
    RCFile.append("## end ltpadmin")
    RCFile.append("")


    #Bpadmin Segment
    RCFile.append("## begin bpadmin")
    RCFile.append("1")
    RCFile.append("a scheme ipn 'ipnfw' 'ipnadminep'")
    #Any more than 1 is unnessary but is good practice as they are essentially ports
    RCFile.append("a endpoint ipn:"+nodeName+".0 q")
    RCFile.append("a endpoint ipn:"+nodeName+".1 q")
    RCFile.append("a endpoint ipn:"+nodeName+".2 q")
    RCFile.append("")
    RCFile.append("a protocol ltp 1400 100")
    # TCP protocol declaration
    RCFile.append("# TCP protocol declaration")
    RCFile.append("a protocol tcp 1400 100")
    RCFile.append("")
    RCFile.append("# LTP and TCP inducts")
    #self Inducts
    RCFile.append("a induct ltp "+nodeName+" ltpcli")
    RCFile.append("a induct tcp "+nodeIP+":4556 tcpcli")
    RCFile.append("")
    #self OutDuct
    RCFile.append("a outduct ltp "+nodeName+" ltpclo")
    RCFile.append("")
    #External Outducs
    for node in primaryNode.connectedNodes:
        connectedIP = str(node.IPAddress[0])+"."+str(node.IPAddress[1])+"."+str(node.IPAddress[2])+"."+str(node.IPAddress[3])
        RCFile.append("a outduct tcp "+connectedIP+":4556 ''")

    # TCP outduct to node 100
    #eg: a outduct tcp 192.168.0.98:4556 ''
    RCFile.append("")
    RCFile.append("s")
    RCFile.append("## end bpadmin")
    RCFile.append("")

    #Begin Ipnadmin Segment
    RCFile.append("## begin ipnadmin")
    RCFile.append("#local")
    RCFile.append("a plan "+nodeName+" ltp/"+nodeName)
    RCFile.append("")

    #Begin IPN Plans of additional Nodes
    RCFile.append("#external")
    for node in primaryNode.connectedNodes:
        connectedIP = str(node.IPAddress[0])+"."+str(node.IPAddress[1])+"."+str(node.IPAddress[2])+"."+str(node.IPAddress[3])
        RCFile.append("a plan 100 tcp/"+connectedIP+":4556")
    
    #eg: a plan 100 tcp/192.168.0.98:4556
    
    RCFile.append("")
    RCFile.append("## end ipnadmin")

    return RCFile
#Write to file
def WriteToFile(RCFile,nodeName):

    output=""
    for line in RCFile:
        output += (line+"\n")
    with io.open(('host'+nodeName+'.rc'), 'w', newline='\n') as f:
        f.write(output)

#User input
def SaveInput(node):
    RCFile = GenerateRC(node)
    WriteToFile(RCFile,node.name)

def GenerateRCFiles(nodes):
    for node in nodes:
        SaveInput(node)
    None