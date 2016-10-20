from Datatypes.Graph import Graph

def getMinimalSpanningtree(graph):
    minimalSpanningtree = Graph()
    tempTree = Graph()
    oldGraph = graph
    treeValue = 0
    for node in oldGraph.getNodes():
        tempTree.addNode(node)
    minimalSpanningtree.addNode(node, True)
    edge = None
    for current_edge in oldGraph.getEdgesOfNode(node.getID()):
        if edge is None:
            edge = current_edge
        elif True:
            pass
    pass

def getSpanningTree(graph):
    spanning_tree = Graph()
    old_graph = graph
    nodes = []
    for node in old_graph.getNodes():
        if node.isTerminal():
            nodes.append(node)
    addable_node = None

    print nodes

    while nodes:
        if addable_node is None:
            addable_node = nodes[0]
            spanning_tree.addNode(addable_node, True)
        else:
            addable_node = nodes[0]
            shortest = None
            if addable_node.isTerminal():
                for edge in old_graph.getEdgesOfNode(addable_node.getID()):
                    if edge.getEndNode().isTerminal():
                        if shortest is None:
                            shortest = edge
                        elif shortest.getValue() > edge.getValue():
                            shortest = edge
                        addable_node = shortest.getEndNode()
            spanning_tree.addNode(addable_node, True)
            spanning_tree.addEdge(spanning_tree.getNodes()[-2].getID(),
                                  spanning_tree.getNodes()[-1].getID(), shortest.getValue())
        addable_node.toString()
        nodes.remove(nodes[0])
    return spanning_tree

