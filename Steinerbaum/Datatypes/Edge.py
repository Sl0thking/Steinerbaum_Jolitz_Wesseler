
class Edge(object):
    '''classdocs'''

    def __init__(self, start_node, end_node, value):
        '''Constructor'''
        self.start_node = start_node
        self.end_node = end_node
        self.value = float(value)

    def getStartNode(self):
        return self.start_node

    def getEndNode(self):
        return self.end_node

    def getValue(self):
        return self.value

    def setStartNode(self, start_node):
        self.start_node = start_node

    def setEndNode(self, end_node):
        self.end_node = end_node

    def setValue(self, value):
        self.value = float(value)

    def __repr__(self):
        return str(self.start_node.getID())+" to "+str(self.end_node.getID())

    def __eq__(self, other):
        return self.getStartNode() == other.getStartNode() and self.getEndNode() == other.getEndNode()

    def toString(self):
        return "Edge from "+str(self.start_node.getID())+" to "+str(self.end_node.getID())+" - VALUE: "+str(self.value)