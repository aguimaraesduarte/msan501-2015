from collections import OrderedDict

def adjlist(adj_list):
    # Read in adj list and store in form of dict mapping node
    # name to list of outgoing edges. Preserve the order you find
    # for the nodes.

    d = OrderedDict()
    lines = adj_list.split("\n")
    for line in lines:
        node = line.split(":")[0]
        target = [t.strip() for t in line.split(":")[1].split(",")]
        d[node] = target

    return d

def adjmatrix(adj):
    # From an adjacency list, return the adjacency matrix with entries in {0,1}.
    # The order of nodes in adj is assumed to be same as they were read in.

    n = len(adj.keys())
    m = [[0 for x in range(n)] for y in range(n)]

    order = {}
    for i in range(n):
        order[adj.keys()[i]] = i

    for i in range(n):
        node = adj.keys()[i]
        node_index = order[node]
        target_list = adj[node]
        for j in range(len(target_list)):
            target_index = order[target_list[j]]
            m[node_index][target_index] = 1

    return m

def nodes(adj, start_node):
    # Walk every node in graph described by adj list starting at start_node
    # using a breadth-first search. Return a list of all nodes found (in
    # any order). Incllude the start_node.

    #visited = []
    #add the start node to a work list;
    #while more work do
        #node = remove a node from work list;
        #add node to visited list;
        #targets = adjacency_list[node];
        #add all unvisited targets to work list;
    #end
    #return visted;

    return 0

adj_list = "parrt: tombu, dmose, parrt\ntombu: dmose, kg9s\ndmose: tombu\nkg9s: dmose"
adj_dict = adjlist(adj_list)
adj_mat = adjmatrix(adj_dict)

print adj_list
print adj_dict
print adj_mat


