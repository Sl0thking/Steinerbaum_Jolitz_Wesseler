
class Node(object):
    '''classdocs'''

    def __init__(self, node_id, is_terminal):
        '''Constructor'''
        self.node_id = node_id
        self.is_terminal = is_terminal

    def isTerminal(self):
        return self.is_terminal

    def getID(self):
        return self.node_id

    def setTerminal(self, is_terminal):
        self.is_terminal = is_terminal

    def __hash__(self, *args, **kwargs):
        return hash(self.getID())

    def __repr__(self):
        return "NODE: "+str(self.getID())+" - Terminal: "+str(self.isTerminal())

    def toString(self):
        return "NODE: "+str(self.getID())+" - Terminal: "+str(self.isTerminal())
