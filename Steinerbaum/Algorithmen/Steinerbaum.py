'''
Created on 18.10.2016

@author: Slothking
'''

from Datatypes.Graph import Graph
from Datatypes.DijsktraGraph import DijsktraGraph
from utilities.utilities import *

def createTestGraph():
    graph = Graph()
    graph.addNode('v_1', True)
    graph.addNode('v_2', True)
    graph.addNode('v_3', True)
    graph.addNode('v_4', True)
    graph.addNode('v_5', False)
    graph.addNode('v_6', False)
    graph.addNode('v_7', False)
    graph.addNode('v_8', False)
    graph.addNode('v_9', False)
    
    graph.addEdge('v_1', 'v_9', 1)
    graph.addEdge('v_1', 'v_2', 10)
    graph.addEdge('v_2', 'v_3', 8)
    graph.addEdge('v_2', 'v_6', 1)
    graph.addEdge('v_3', 'v_4', 9)
    graph.addEdge('v_3', 'v_5', 2)
    graph.addEdge('v_4', 'v_5', 2)
    graph.addEdge('v_5', 'v_6', 1)
    graph.addEdge('v_5', 'v_9', 1)
    graph.addEdge('v_6', 'v_7', 1)
    graph.addEdge('v_7', 'v_8', 0.5)
    graph.addEdge('v_8', 'v_9', 0.5)
    
    return graph

if __name__ == '__main__':
    kevin1 = False
    graph = createTestGraph()
    #graph.toString()

    if kevin1:
            #graph.toString()
            dijkstra_graph = DijsktraGraph()
            dijkstra_graph.importFromGraph(graph)
            shortest_paths = []
            
            terminals = graph.getTerminals()
            #print terminals
            for start_terminal_id in terminals:
                for end_terminal_id in terminals:
                    if(start_terminal_id != end_terminal_id):
                        #print "DIJKSTRA START: " + start_terminal_id + " END: " + end_terminal_id
                        short_graph = dijkstra_graph.getShortestPath(start_terminal_id, end_terminal_id)
                        #print short_graph.toString()
                        print "A: " + start_terminal_id + " - E: " + end_terminal_id
                        short_graph.toString()
                        shortest_paths.append(short_graph)
            #Build Distance Graph
            distance_graph = Graph()
            for path in shortest_paths:
                #path.toString()
                start_end_node = path.getTerminals()
                print start_end_node
                if len(start_end_node) == 2:
                    distance_graph.addNode(start_end_node[0], True)
                    distance_graph.addNode(start_end_node[1], True)
                    edgeValue = path.getSumOfEdges()
                    distance_graph.addEdge(start_end_node[0], start_end_node[1], edgeValue)
            distance_graph.toString()
    else:
        print "_________________"
        print "-- normalgraph --"
        graph.toString()
        print "_________________"
        print "------ MST ------"
        getMinimalSpanningtree(graph).toString()
