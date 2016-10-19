'''
Created on 18.10.2016

@author: Slothking
'''

import Graph
import DijkstraNode

class DijsktraGraph(Graph):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def importFromGraph(self, graph):
        nodes = graph.getNodes()
        for node in nodes:
            self.addNode(node.getID(), node.isTerminal())
        
        edges = graph.getEdges()
        
        for edge in edges:
            self.addEdge(edge.getStartNode().getID(), edge.getEndNode().getID(), edge.getValue())
                
    
    def addNode(self, node_id, is_terminal):
        # adds node to the nodeMap as key
        node = DijkstraNode(node_id, is_terminal)
        self.__nodeMap[node] = []
    