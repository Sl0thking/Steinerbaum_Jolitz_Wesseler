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
    wait = raw_input()
    shortest_paths = getShortestPaths(graph)
    distance_graph = getDistanceGraph(graph, shortest_paths)
    print "############################################"
    print "#               Distance Graph             #"
    print "############################################"
    print distance_graph
    wait = raw_input()
    min_distance_graph = getMinimalSpanningtree(distance_graph)
    transform_graph = transformDistanceToSteinerbaum(min_distance_graph, shortest_paths)
    print "############################################"
    print "#                Steinerbaum               #"
    print "############################################"
    print transform_graph
