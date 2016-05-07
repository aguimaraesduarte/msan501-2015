from graphs import *

adj_list = "parrt: tombu, dmose, parrt\ntombu: dmose, kg9s\ndmose: tombu\nkg9s: dmose"
#adj_list = \
#"""
#parrt: tombu, dmose, parrt
#tombu: dmose, kg9s
#dmose: tombu
#kg9s: dmose
#"""
adj_dict = adjlist(adj_list)
adj_mat = adjmatrix(adj_dict)
visited = nodes(adj_list, 'parrt')
dot = gendot(adj_list)

#print adj_list
#print adj_dict
#print adj_mat
#print visited
print dot