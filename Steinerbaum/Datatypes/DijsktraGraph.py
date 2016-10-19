'''
Created on 18.10.2016

@author: Slothking
'''

from Graph import Graph
from DijkstraNode import DijkstraNode

class DijsktraGraph(Graph):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DijsktraGraph, self).__init__()
    
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
        super(DijsktraGraph, self).addNodeToMap(node)
    
    def getShortestPath(self, start_node_id, end_note_id):
        if(start_node_id == end_note_id):
            return None
        else:
            self.prepare_graph(start_node_id)
            unvisited_nodes = self.getNodes()
            current_node = self.getNodeWithMinDistance(unvisited_nodes)
            while len(unvisited_nodes) > 0 and current_node != None and current_node.getID() == end_note_id:
                neighbour_edges = self.getEdgesOfNode(current_node.getID())
                for edge in neighbour_edges:
                    neighbour_node = edge.getEndNode()
                    if neighbour_node.isVisited() == False:
                        possible_distance = current_node.getDistance() + edge.getValue()
                        if(neighbour_node.getDistance() == -1 or neighbour_node.getDistance() > possible_distance):
                            neighbour_node.setDistance(possible_distance)
                            neighbour_node.setPrevNode(current_node)
                unvisited_nodes.remove(current_node)
                current_node.setIsVisited(True)
                current_node = self.getNodeWithMinDistance(unvisited_nodes)
            return self.constructGraph(self.getNode(end_note_id))

    def getNodeWithMinDistance(self, unvisited_nodes):
        if(len(unvisited_nodes) > 0):
            min_node = unvisited_nodes[0]
            for node in unvisited_nodes:
                if node.getDistance() < min_node.getDistance():
                    min_node = node
            return min_node
        else:
            return None
    
    def constructGraph(self, end_node):
        graph = Graph()
        current_node = end_node
        while(current_node.getPrevNode() != None):
            graph.addNode(current_node)
            graph.addNode(current_node.getPrevNode())
            graph.addEdge(current_node.getID(), current_node.getPrevNode().getID(), (current_node.getPrevNode.getDistance() - current_node.getDistance()))
        return graph
    
    def prepare_graph(self, start_node_id):
        nodes = self.getNodes()
        for node in nodes:
            if node.getID() == start_node_id:
                node.setIsVisited(False)
                node.setDistance(-1)
                node.setPrevNode(None)
            else:
                node.setIsVisited(True)
                node.setDistance(0)
                node.setPrevNode(None)