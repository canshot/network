import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('C:/Users/jlim13/Google Drive/3. 2018 Fall Class/ITIS 8520 Network Science/assignment/In-class Assignment2/soc-sign-Slashdot081106.txt', nodetype=int,
  data=(('sign',int),), create_using=nx.Graph())

print(g.edges(data=True))

print(nx.info(g))

"""
Q1. Number of triangles in the network
"""
print(nx.triangles(g,0))
#649 

"""
Q2. Report the fraction of balanced triangles and unbalanced triangles
"""

import numpy as np
triangles = [c for c in nx.cycle_basis(g) if len(c)==3]
triangle_types={}
for triangle in triangles:
    tri=nx.subgraph(g,triangle)
    #take the product of the edge relationships. If there are an odd number of -1s, the triangle is unbalanced.
    triangle_types[tuple(tri.nodes())]=np.product([x[2]['sign'] for x in tri.edges(data=True)])
print(triangle_types)

#value =1 if it is balanced, =-1 if unbalanced.
