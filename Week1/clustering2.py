import utils
from Node import *
from pprint import *
from itertools import *
import winsound

def merge_old(surviving_leader, dead_leader, clusters):
    if surviving_leader == dead_leader:
        raise Exception()
    
    for node in clusters[dead_leader]:
        node.leader = surviving_leader
    clusters[surviving_leader].extend(clusters[dead_leader])
    del clusters[dead_leader]

def generate_neighbours(value):
    length = len(value)    
    for i in range(length):
        l = bytearray(value, 'utf8')
        l[i] = 48 if l[i] == 49 else 49  # 48 is ord('0'), 49 is ord('1')
        yield l.decode()
    for i in range(length - 1):
        for j in range(i + 1, length):
            l = bytearray(value, 'utf8')
            l[i] = 48 if l[i] == 49 else 49  # 48 is ord('0'), 49 is ord('1')
            l[j] = 48 if l[j] == 49 else 49  # 48 is ord('0'), 49 is ord('1')
            yield l.decode()

def merge(c1, c2, nodes, clusters):
    clusters[c1].extend(clusters[c2])
    for v in clusters[c2]:
        nodes[v] = c1
    #del clusters[c2]    

if __name__ == "__main__":
    # filename = "clustering_small.txt"    
    filename = "clustering_big.txt"    
    with open(filename, "r") as file:
        lines = file.readlines()
        n = int(lines[0].split(' ')[0])
        # l = int(lines[0].split(' ')[1])
        lines = lines[1:n + 1]

    # first we have each node in it's own cluster - dict key is the leader for each cluster (starts with Node index)
    nodes = {}
    for line in lines:
        value = ''.join(line.split())
        if value in nodes:
            n -= 1
        else:
            nodes[ value ] = value # leader for each cluster            

    clusters = { value: [ value ] for value in nodes.keys() } 
    
    for node in nodes:
        for v in generate_neighbours(node):
            if v in nodes:
                c1 = nodes[node]
                c2 = nodes[v]
                if(c1 != c2):    #check nodes already in same cluster                 
                    if(len(clusters[c1]) > len(clusters[c2])):
                        merge(c1, c2, nodes, clusters)  
                    else:
                        merge(c2, c1, nodes, clusters)  
                    n -= 1
                    pprint("N: " + str(n))

    # pprint("N: " + str(n))
    #Voc
    Freq = 2500 # Set Frequency To 2500 Hertz
    Dur = 500 # Set Duration To 1000 ms == 1 second
    winsound.Beep(Freq,Dur)