
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
        self.__nodeMap[node] = []
    
    def addNodeToMap(self, node):
        self.__nodeMap[node] = []
        
    def addEdge(self, start_node_id, end_node_id, value):
        # adds the edge to the nodeMap. Will be insert in the list_of_edges of the node-key
        try:
            for node in self.__nodeMap.keys():
                if node.getID() == start_node_id:
                    start_node = node
                if node.getID() == end_node_id:
                    end_node = node

            start = True
            for edge in self.__nodeMap[start_node]:
                if edge.getStartNode().getID() == start_node_id:
                    start = False
            if start:
                new_edge = Edge(start_node, end_node, value)
                self.__nodeMap[start_node].append(new_edge)

            end = True
            for edge in self.__nodeMap[end_node]:
                if edge.getEndNode().getID() == end_node_id:
                    end = False
            if end:
                new_edge = Edge(end_node, start_node, value)
                self.__nodeMap[end_node].append(new_edge)

        except Exception, e:
            print "EXCEPTION in Graph.addEdge "+str(e)

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
       

    def getEdgesOfNode(self, node_id):
        edges = []
        for node in self.__nodeMap.keys():
            if node.getID() == node_id:
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
                print edge.toString()
