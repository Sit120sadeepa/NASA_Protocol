from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

# Stuff for generating the network visualization to be passed to the UI
def GenerateGraph(nodes):
    # Deep Clone
    nodeCopy = deepcopy(nodes)

    nodeCount = len(nodeCopy)

    # Create an empty undirected networkx graph
    g = nx.Graph()

    # Add nodes
    g.add_nodes_from(range(nodeCount))

    nodeList = []
    for node in nodes:
        nodeList.append(node.name)

    # Add labels to nodes
    node_labels = {i: str(nodeList[i]) for i in range(nodeCount)}

    edges = []

    # Generate Edges
    for i in range(nodeCount):
        for j in range(nodeCount):
            inode = nodeCopy[i]
            jnode = nodeCopy[j]
            if inode.connectedNodes.count(jnode) > 0:
                edges.append((i, j))
                try:
                    jnode.connectedNodes.remove(inode)
                except:
                    None

    # Add edges
    g.add_edges_from(edges)

    # Draw the graph
    pos = nx.spring_layout(g)  # You can choose a different layout algorithm if needed
    node_colors = ['white' for _ in range(nodeCount)]

    # Set node properties
    nx.draw(
        g,
        pos=pos,
        with_labels=True,
        labels=node_labels,
        node_size=200,  # You can adjust the node size as needed
        node_color=node_colors,
        edge_color='black',
        font_size=10,
    )

    plt.axis('off')
    plt.tight_layout()

    return plt.gcf()