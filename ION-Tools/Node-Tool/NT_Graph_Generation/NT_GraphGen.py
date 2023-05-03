from copy import deepcopy
import igraph as ig
import matplotlib.pyplot as plt

#Stuff for generating Graph

def GenerateGraph(nodes):
    #Deep Clone
    nodeCopy = deepcopy(nodes)

    nodeCount = len(nodeCopy)

    g = ig.Graph(directed=False)

    # Add 5 vertices
    g.add_vertices(nodeCount)

    nodeList = []
    for node in nodes:
       nodeList.append(node.name)


    # Add ids and labels to vertices
    for i in range(len(g.vs)):
        g.vs[i]["id"]= i
        g.vs[i]["label"]= str(nodeList[i])  #str(i)

    edges = []

    #Generate Edges
    for i in range(nodeCount):
        for j in range (nodeCount):
            inode = nodeCopy[i]
            jnode = nodeCopy[j]
            if(inode.connectedNodes.count(jnode)>0):
                edges.append((i,j))
                try: jnode.connectedNodes.remove(inode)
                except:None
    # Add edges
    g.add_edges(edges)

    visual_style = {}

    #Colour of the line between nodes
    visual_style["edge_color"] = 'black'

    #node properties
    #size of the text inside the node
    visual_style["vertex_label_size"] = 10
    #Node inside colour
    visual_style["vertex_color"] = 'white'

    fig, ax = plt.subplots()
    ig.plot(g, target=ax,**visual_style)
    
    return fig