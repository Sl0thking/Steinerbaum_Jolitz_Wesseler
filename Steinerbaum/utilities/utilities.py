from Datatypes.Graph import Graph

def getMinimalSpanningtree(graph):
    msp = Graph()
    oldGraph = graph
    #visited_nodes = []
    msp.addNode(oldGraph.getNodes()[0].getID(), oldGraph.getNodes()[0].isTerminal())
    #visited_nodes.append(oldGraph.getNodes()[0].getID())
    count = 0
    while oldGraph.getNodes() != msp.getNodes() or count > 10:
        count+=count
        for node in oldGraph.getNodes():
            #print "##### CURNODE: "+str(node)
            #print "OLD: "+str(oldGraph.getNodes())
            #print "MSP: "+str(msp.getNodes())
            finalEdge = None
            for msp_node in msp.getNodes():
                #print "MSPNODE: "+str(msp_node)
                for edge in oldGraph.getEdgesOfNode(msp_node.getID()):
                    #print edge
                    if finalEdge is None:
                        finalEdge = edge
                    else:
                        if edge.getValue() < finalEdge.getValue() and edge.getEndNode() not in msp.getNodes():
                            finalEdge = edge
            if finalEdge.getEndNode() not in msp.getNodes():
                #print "ADD NODE: "+str(finalEdge.getEndNode().getID())
                msp.addNode(finalEdge.getEndNode().getID(), finalEdge.getEndNode().isTerminal())
                #print msp.toString()
                #print "ADD EDGE: "+str(finalEdge)
                msp.addEdge(finalEdge.getStartNode().getID(), finalEdge.getEndNode().getID(), finalEdge.getValue())
        msp.addNode(node.getID(), node.isTerminal())
    return msp

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
