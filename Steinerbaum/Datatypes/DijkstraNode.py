'''
Created on 19.10.2016

@author: Slothking
'''

import Node

class DijkstraNode(Node):
    '''
    classdocs
    '''
    
    def getDistance(self):
        return self.distance
    
    def setDistance(self, distance):
        self.distance = distance
    
    def setIsVisited(self, visited):
        self.is_visited = visited
        
    def isVisited(self):
        return self.is_visited

    def __init__(self, node_id, is_terminal):
        '''
        Constructor
        '''
        super(node_id, is_terminal)
        distance = -1
        is_visited = False