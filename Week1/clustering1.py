import utils
import heapq
from Node import *
from pprint import *
from DynamicKeyHeap import DynamicKeyHeap
        
def merge(u, v, clusters):
    dead_leader = v.leader
    surviving_leader = u.leader
    for node in clusters[dead_leader]:
        node.leader = surviving_leader
    clusters[surviving_leader].extend(clusters[dead_leader])
    del clusters[dead_leader]

if __name__ == "__main__":
    # graph = utils.read_graph("clustering1.txt")
    N, edges = utils.read_edges("clustering1.txt")
    
    # first we have each node in it's own cluster - dict key is the leader for each cluster
    clusters = {x:[Node(x, x)] for x in range(1, N + 1)}

    # creates edges list in form (Node,Node,cost) - same node references in the clusters
    # need this so when I update leader (aka cluster) info I get the ref updated
    edges = [[clusters[int(i[0])][0], clusters[int(i[1])][0], int(i[2])] for i in edges]

    sorted_edges = DynamicKeyHeap(edges, lambda edge: edge[2]) # heapify by edge' cost
    
    max_spacing = 0
    while len(clusters) >= 4:
        min_edge = sorted_edges.pop_value() #get min value
        u = min_edge[0]
        v = min_edge[1]
        cost = min_edge[2]
        
        if(u.leader == v.leader):
            continue;                
        
        if(len(clusters) == 4):
            max_spacing = cost
            break
        # merge clusters
        u_friends = clusters[u.leader]
        v_friends = clusters[v.leader]

        if(len(u_friends) > len(v_friends)):
            merge(u, v, clusters)
        else:
            merge(v, u, clusters)   

    pprint("Max spacing of 4 clusters: " + str(max_spacing))