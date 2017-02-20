def read_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        lines = [l.rstrip() for l in lines]
    return lines

def init_graf(nodes_count, edges, duplicate):
    """
    Creates a dict with each key being a Node and the value a list of [(sink, cost), ...]

    Note: All nodes have keys so the info is redundant. You can find an edge in both it's Nodes entries

    Returns:
    graph = dict: {source: [(sink, cost), ...], ...} (format)
    """
    graph = {el:[] for el in range(1, nodes_count + 1)} 
    for edge in edges:
        source = int(edge[0])    
        sink = int(edge[1])
        cost = int(edge[2])
        graph[source].append((sink, cost))
        if(duplicate):            
            graph[sink].append((source, cost))
    return graph

def read_edges(filename):
    lines = read_lines(filename)
    nodes_count = int(lines[0].split(' ')[0])

    # [[source, sink, cost], ...] list
    edges = [l.split(' ') for l in lines[1:]]   
    return (nodes_count,edges)

def read_graph(fileName, duplicate = False):
    """
    Read a graph from a file formated
    N 
    i j cost
    ...

    Returns:
    graph = dict: {source: [(sink, cost), ...], ...} (format)
    """
    lines = read_lines(fileName)
    nodes_count = int(lines[0].split(' ')[0])

    # [[source, sink, cost], ...] list
    edges = [l.split(' ') for l in lines[1:]]   

    graph = init_graf(nodes_count, edges, duplicate)
    return graph    