'''
Created on 18.10.2016

@author: Slothking
'''

from Datatypes.Graph import Graph
from utilities.utilities import *

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

    graph.addEdge('v_1', 'v_9', 1)
    graph.addEdge('v_1', 'v_2', 10)
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
'''
def getShortestPath(start_node_id, end_note_id, graph):
    if(start_node_id == end_note_id):
        return None
    else:
        graph_copy = graph #TO DO DEEP COPY
        start_node = graph_copy.getNode(start_node_id)
        start_node.setValue(0)
        start_node.setIsVisited(True)
        
        current_node = start_node
        
        while 
        start_edges = graph.getEdges(start_node_id)
        for edge in start_edges:
            endNode = edge.getEndNode()
            if(endNode.isVisited() != True):
                    endNode.setValue(start_node.getValue() + edge.getValue())
    
def getMinDistance(node_id, graph):
    minDistanceNode = None
    for edge in graph.getEdges(node_id):
        endNode = edge.getEndNode()
        if(minDistanceNode == None or minDistanceNode.getValue() < endNode.getValue()):
            minDistanceNode = endNode
    return minDistanceNode


            
def sumShortestPath(end_node):
    sum = 0
    current_node = end_node
    while current_node.getBefore() != None:
        sum += current_node.getValue()
        current_node = current_node.getBefore()
    return sum   
'''
if __name__ == '__main__':
    graph = createTestGraph()
    print "_________________"
    graph.toString()
    print "_________________"
    getSpanningTree(graph).toString()
    ''' 
    terminals = graph.getTerminals()
    for start_terminal_id in terminals:
        for end_terminal_id in terminals:
            node_ids = getShortestPath(start_terminal_id, end_terminal_id, graph)
            if(node_ids != None):
    '''            
    
