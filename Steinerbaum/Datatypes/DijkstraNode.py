'''
Created on 19.10.2016

@author: Slothking
'''

from Node import Node

class DijkstraNode(Node):
    '''
    classdocs
    '''
    
    def getDistance(self):
        return self.distance
    
    def setDistance(self, distance):
        self.distance = distance
    
    def getPrevNode(self):
        return self.prev_node
    
    def setPrevNode(self, node):
        self.prev_node = node
        
    def isVisited(self):
        return self.is_visited
    
    def setIsVisited(self, visited):
        self.is_visited = visited
    
    def __init__(self, node_id, is_terminal):
        '''
        Constructor
        '''
        super(DijkstraNode, self).__init__(node_id, is_terminal)
        distance = -1
        is_visited = False
        prev_node = None