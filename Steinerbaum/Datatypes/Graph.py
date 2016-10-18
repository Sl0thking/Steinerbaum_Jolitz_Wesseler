
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
    
    def addEdge(self, start_node_id, end_node_id, value):
        # adds the edge to the nodeMap. Will be insert in the list_of_edges of the node-key
        try:
            for node in self.__nodeMap.keys():
                if node.getID() == start_node_id:
                    start_node = node
                if node.getID() == end_node_id:
                    end_node = node

            start = False
            for edge in self.__nodeMap[start_node_id]:
                if edge.getStartNode().getID() == start_node_id:
                    start = True
            if start:
                new_edge = Edge(start_node, end_node, value)
                self.__nodeMap[start_node_id].append(new_edge)

            end = False
            for edge in self.__nodeMap[end_node_id]:
                if edge.getEndNode().getID() == end_node_id:
                    end = True
            if end:
                new_edge = Edge(end_node, start_node, value)
                self.__nodeMap[end_node_id].append(new_edge)

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

    def getEdges(self, node_id):
        edges = []
        for edge in self.__nodeMap[node_id]:
            edges.append(edge)
        return edges

    def getTerminals(self):
        # return array with the IDs of terminal-nodes
        terminal_list = []
        for node in self.__nodeMap.keys():
            if node.isTerminal():
                terminal_list.append(node.getID())
        return terminal_list
