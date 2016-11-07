'''
Created on 18.10.2016

@author: Slothking
'''

from Datatypes.Graph import Graph
from Datatypes.DijsktraGraph import DijsktraGraph
from utilities.utilities import *

if __name__ == '__main__':
    graph = createTestGraph()
    print "############################################"
    print "#         Distance network heuristic       #"
    print "############################################"
    print "--------------------------------------------"
    print "############################################"
    print "#                Source graph              #"
    print "############################################"
    print graph
    wait = raw_input("...")
    shortest_paths = getShortestPaths(graph)
    distance_graph = getDistanceGraph(graph, shortest_paths)
    print "############################################"
    print "#     1. Calculated Distance Graph         #"
    print "############################################"
    print distance_graph
    wait = raw_input("...")
    min_distance_graph = getMinimalSpanningtree(distance_graph)
    print "############################################"
    print "#      2. minimal Distance Graph           #"
    print "############################################"
    print min_distance_graph
    wait = raw_input("...")
    transform_graph = transformDistanceToSteinerbaum(min_distance_graph, shortest_paths)
    print "############################################"
    print "#        3. transformed Graph             #"
    print "############################################"
    print transform_graph
    wait = raw_input("...")
    min_transform_graph = getMinimalSpanningtree(transform_graph)
    print "############################################"
    print "#      4. minimal transformed Graph        #"
    print "############################################"
    print min_transform_graph
    wait = raw_input("...")
    nodes = min_transform_graph.getNodes()
    
    for node in nodes:
        edges = min_transform_graph.getEdgesOfNode(node.getID())
        if len(edges) < 2 and not node.isTerminal():
            min_transform_graph.delNode(node.getID())
    print "############################################"
    print "#             5. Steinerbaum               #"
    print "############################################"
    print min_transform_graph