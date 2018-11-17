import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('***/soc-sign-Slashdot081106.txt', nodetype=int,
  data=(('sign',int),), create_using=nx.Graph())

print(g.edges(data=True))

print(nx.info(g))

