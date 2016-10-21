from Datatypes.Graph import Graph
import time

def getMinimalSpanningtree(graph):
    msp = Graph()
    old_graph = graph
    msp.addNode(old_graph.getNodes()[0].getID(), old_graph.getNodes()[0].isTerminal())
    while old_graph.getNodes() != msp.getNodes():
        for node in old_graph.getNodes():
            print "##### CURNODE: "+str(node)
            print "OLD: "+str(old_graph.getNodes())
            print "MSP: "+str(msp.getNodes())
            final_edge = None
            for msp_node in msp.getNodes():
                #time.sleep(2)
                print "MSPNODE: "+str(msp_node)
                #print "MSPEDGE: "+str(old_graph.getEdgesOfNode(msp_node.getID()))
                for edge in old_graph.getEdgesOfNode(msp_node.getID()):
                    if final_edge is None:
                        final_edge = edge
                    else:
                        if edge.getEndNode() not in msp.getNodes():
                            final_edge = edge
                    #print final_edge
            print str(final_edge.getEndNode())+" - "+str(msp.getNodes())
            if final_edge.getEndNode() not in msp.getNodes():
                #print "ADD NODE: "+str(final_edge.getEndNode().getID())
                msp.addNode(final_edge.getEndNode().getID(), final_edge.getEndNode().isTerminal())
                #print "ADD EDGE: "+str(final_edge)
                msp.addEdge(final_edge.getStartNode().getID(), final_edge.getEndNode().getID(), final_edge.getValue())
        #msp.addNode(node.getID(), node.isTerminal())
        #print "ADDED NODE: "+str(node)
        #msp.toString()
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
