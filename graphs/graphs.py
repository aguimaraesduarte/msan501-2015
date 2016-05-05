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

    for key in adj.keys():
        print adj[key]

    print m

    return 0

adj_list = "parrt: tombu, dmose, parrt\ntombu: dmose, kg9s\ndmose: tombu\nkg9s: dmose"
adj_dict = adjlist(adj_list)
print adj_dict
print adjmatrix(adj_dict)


