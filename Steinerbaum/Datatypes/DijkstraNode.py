'''
Created on 19.10.2016

@author: Slothking
'''

from Node import Node

class DijkstraNode(Node):
    '''
    classdocs
    '''
    def __init__(self, node_id, is_terminal):
        '''
        Constructor
        '''
        super(DijkstraNode, self).__init__(node_id, is_terminal)
        distance = -1
        is_visited = False
        prev_node = None
        
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
    
    def __str__(self):
        string_rep = "NODE: "+str(self.node_id)
        string_rep += " - Terminal: "+str(self.is_terminal) 
        string_rep += " - Visited: " + str(self.is_visited)
        string_rep += " - Distance: " + str(self.distance)
        if(self.prev_node != None):
            string_rep +" - Prev: " + str(self.prev_node)
        else:
            string_rep +" - Prev: NONE"
        return string_rep