import networkx as nx

g = nx.Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)

g.add_edge(1,2)
g.add_edge(2,1)
g.add_edge(1,3)
g.add_edge(1,1)

#1. The number of nodes in the network
g.number_of_nodes()
#outcome = 3

#2. The number of self-edge in the network
g.number_of_selfloops()
#outcome = 1

#3. The number of directed edges in the network
g.number_of_edges()
#outcome = 4
