from Datatypes.Graph import Graph
from Datatypes.DijsktraGraph import DijsktraGraph

def createTestGraph():
    graph = Graph()
    graph.addNode('v_1', True)
    graph.addNode('v_2', True)
    graph.addNode('v_3', True)
    graph.addNode('v_4', True)
    graph.addNode('v_5', False)
    graph.addNode('v_6', False)
    graph.addNode('v_7', False)
    graph.addNode('v_8', False)
    graph.addNode('v_9', False)
    #graph.addNode('kill', False)
    
    graph.addEdge('v_1', 'v_9', 1)
    graph.addEdge('v_1', 'v_2', 10)
    #graph.addEdge('v_1', 'kill', 40)
    #graph.addEdge('kill', 'v_2', 50)
    graph.addEdge('v_2', 'v_3', 8)
    graph.addEdge('v_2', 'v_6', 1)
    graph.addEdge('v_3', 'v_4', 9)
    graph.addEdge('v_3', 'v_5', 2)
    graph.addEdge('v_4', 'v_5', 2)
    graph.addEdge('v_5', 'v_6', 1)
    graph.addEdge('v_5', 'v_9', 1)
    graph.addEdge('v_6', 'v_7', 1)
    graph.addEdge('v_7', 'v_8', 0.5)
    graph.addEdge('v_8', 'v_9', 0.5)
    
    return graph

def getShortestPaths(graph):
    dijkstra_graph = DijsktraGraph()
    dijkstra_graph.importFromGraph(graph)
    shortest_paths = {}
    terminals = graph.getTerminals()
    for start_terminal_id in terminals:
        for end_terminal_id in terminals:
            if(start_terminal_id != end_terminal_id):
                short_graph = dijkstra_graph.getShortestPath(start_terminal_id, end_terminal_id)
                shortest_paths[(start_terminal_id, end_terminal_id)] = short_graph
    return shortest_paths

def getDistanceGraph(graph, shortest_paths):
    #Build Distance Graph
    distance_graph = Graph()
    terminals = graph.getTerminals()
    for x in terminals:
        for y in terminals:
            if x != y:
                start_end_node = shortest_paths[(x, y)].getTerminals()
                distance_graph.addNode(start_end_node[0], True)
                distance_graph.addNode(start_end_node[1], True)
                edgeValue = shortest_paths[(x, y)].getSumOfEdges()
                distance_graph.addEdge(start_end_node[0], start_end_node[1], edgeValue)
    return distance_graph

def transformDistanceToSteinerbaum(min_distance_graph, shortest_paths):
    transform_graph = Graph()
    edges = min_distance_graph.getEdges()
    for edge in edges:
        start_node = edge.getStartNode()
        end_node = edge.getEndNode()
        if start_node != end_node:
            shortest_path = shortest_paths[(start_node.getID(), end_node.getID())]
            for node in shortest_path.getNodes():
                transform_graph.addNode(node.getID(), node.isTerminal())
            for edge in shortest_path.getEdges():
                transform_graph.addEdge(edge.getStartNode().getID(), edge.getEndNode().getID(), edge.getValue())
    return transform_graph

def getMinimalSpanningtree(graph):
    msp = Graph()
    old_graph = graph
    msp.addNode(old_graph.getNodes()[0].getID(), old_graph.getNodes()[0].isTerminal())
    while old_graph.getNodes() != msp.getNodes():
        for node in old_graph.getNodes():
            final_edge = None
            for msp_node in msp.getNodes():
                for edge in old_graph.getEdgesOfNode(msp_node.getID()):
                    if final_edge is None:
                        final_edge = edge
                    else:
                        if edge.getEndNode() not in msp.getNodes():
                            final_edge = edge
            if final_edge.getEndNode() not in msp.getNodes():
                msp.addNode(final_edge.getEndNode().getID(), final_edge.getEndNode().isTerminal())
                msp.addEdge(final_edge.getStartNode().getID(), final_edge.getEndNode().getID(), final_edge.getValue())
    return msp
