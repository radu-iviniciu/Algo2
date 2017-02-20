from pprint import *
from heapq import *
import os, sys, inspect
from DynamicKeyHeap import DynamicKeyHeap
from Node import Node
    
if __name__ == '__main__':
    with open("week3\huffman.txt") as f:
        lines = f.readlines()
        count = lines[0]
        lines = lines[1:]

    nodes = [Node(int(w)) for w in lines]
    heap = DynamicKeyHeap(nodes, lambda node: node.weight())
    while (heap.length() > 1):
        a = heap.pop_value()
        b = heap.pop_value()
        a.append('0')
        b.append('1')        
        heap.push(Node(a.weight() + b.weight(), a, b))

    max_code_lenght = max([len(n.code()) for n in nodes])
    min_code_lenght = min([len(n.code()) for n in nodes])
    pprint("Max code word: " + str(max_code_lenght))
    pprint("Min code word: " + str(min_code_lenght))