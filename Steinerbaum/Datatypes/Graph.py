
from Edge import Edge
from Node import Node

class Graph(object):
    '''classdocs'''

    def __init__(self):
        '''Constructor'''
        self.__nodeMap = {} #{1:list_of_edges, 2:}

    def addNode(self, node_id, is_terminal):
        # adds node to the nodeMap as key
        node = Node(node_id, is_terminal)
        self.addNodeToMap(node)
        
    def addNodeToMap(self, node):
        if not (self.__nodeMap.has_key(node)):
            self.__nodeMap[node] = []
        
    def addEdge(self, start_node_id, end_node_id, value):
        for node in self.__nodeMap.keys():
            if node.getID() == start_node_id:
                start_node = node
            if node.getID() == end_node_id:
                end_node = node
        if not self.edgeExist(start_node, end_node):
            new_edge = Edge(start_node, end_node, value)
            self.__nodeMap[start_node].append(new_edge)
            new_edge = Edge(end_node, start_node, value)
            self.__nodeMap[end_node].append(new_edge)

    def edgeExist(self, start_node, end_node):
        start_edges = self.getEdgesOfNode(start_node.getID())
        end_edges = self.getEdgesOfNode(end_node.getID()) 

        start_to_end_exists = False
        end_to_start_exists = False
        
        for edge in start_edges:
            if edge.getStartNode() == start_node and edge.getEndNode() == end_node:
                start_to_end_exists = True
                
        for edge in end_edges:
            if edge.getStartNode() == end_node and edge.getEndNode() == start_node:
                end_to_start_exists = True
        
        return start_to_end_exists and end_to_start_exists
    

    def modifyEdgeValue(self, start_node_id, end_node_id, value):
        for edge_list in self.__nodeMap.values():
            for edge in edge_list:
                if edge.getStartNode.getID() == start_node_id and edge.getEndNode.getID() == end_node_id:
                    edge.setValue(value)
    
    def delNode(self, node_id):
        del self.__nodeMap[node_id]
        for edge_list in self.__nodeMap.values():
            for edge in edge_list:
                if edge.getStartNode.getID() == node_id or edge.getEndNode.getID() == node_id:
                    del edge

    def delEdge(self, start_node_id, end_node_id):
        for edge_list in self.__nodeMap.values():
            for edge in edge_list:
                if edge.getStartNode.getID() == start_node_id and edge.getEndNode.getID() == end_node_id:
                    del edge

    def getNode(self, node_id):
        for node in self.__nodeMap.keys():
            if node.getID() == node_id:
                return node
        raise Exception("None Node Found!")

    def getNodes(self):
        return self.__nodeMap.keys()
       
    def getSumOfEdges(self):
        edges_sum = 0
        for edge in self.getEdges():
            edges_sum += edge.getValue()
        return edges_sum / 2 #Every Edge is doubled for both directions
    
    def getEdgesOfNode(self, node_id):
        edges = []
        for node in self.__nodeMap.keys():
            cur_id = node.getID()
            if cur_id == node_id:
                for edge in self.__nodeMap[node]:
                    edges.append(edge)
        return edges

    def getEdges(self):
        edges = []
        for node in self.__nodeMap.keys():
            for edge in self.__nodeMap[node]:
                edges.append(edge)
        return edges

    def getTerminals(self):
        # return array with the IDs of terminal-nodes
        terminal_list = []
        for node in self.__nodeMap.keys():
            if node.isTerminal():
                terminal_list.append(node.getID())
        return terminal_list

    def toString(self):
        for key in self.__nodeMap.keys():
            print "KEY: "+key.toString()
            for edge in self.getEdgesOfNode(key.getID()):
                print "\t"+edge.toString()
     
    def __str__(self):
        return_str = ""
        for key in self.__nodeMap.keys():
            return_str += key.toString() + "\n"
            for edge in self.getEdgesOfNode(key.getID()):
                return_str += "\t" +edge.toString() + "\n"
        return return_str
    
    def __repr__(self):
        return_str = ""
        for key in self.__nodeMap.keys():
            return_str += key.toString() + "\n"
            for edge in self.getEdgesOfNode(key.getID()):
                return_str += "\t" +edge.toString() + "\n"
        return return_str
                