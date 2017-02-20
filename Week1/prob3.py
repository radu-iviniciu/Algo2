"""
In this programming problem you'll code up Prim's minimum spanning tree algorithm.

Download the text file below.

edges.txt
This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""

import utils
import math
from heapq import *
from pprint import *

from DynamicKeyHeap import *

def get_min_edge_cost(source, sink, graph):
    """
    Gets the cost of the edage between the source and the sink.     

    Returns Inf  if there is no direct ebdge between the two
    """
    result = [c for s,c in graph[source] if s == sink]
    if(any(result)):
        return result[0]
    return math.inf 

if __name__ == "__main__":
    graph = utils.read_graph("edges.txt", True)

    #init spannning treew with first node
    X = [1] # nodes in the spanning Tree so far
    V_X = graph # remaining nodes
    del V_X[1]
    TCost = 0 # total cost of spanning tree so far

    # init Min Const of crossing Tree Heap. (Heap contains (Key,Value) pairs => Key - min cost, value - remNode pairs)
    minCrossingCostHeap = DynamicKeyHeap(V_X.keys(), lambda remainingNode: get_min_edge_cost(remainingNode, 1, V_X))
    
    while any(V_X):
        minCost, poppedNode = minCrossingCostHeap.pop_kvp()
        TCost += minCost
        X.append(poppedNode)
        del V_X[poppedNode]
        minCrossingCostHeap.update_data(lambda remainingNode: get_min_edge_cost(remainingNode, poppedNode, V_X))

    pprint("Min cost sum of spanning Tree: " + str(TCost))