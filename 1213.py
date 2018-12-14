import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import networkx as nx

# for Notebook
%matplotlib inline

uid_reuid = dict()
with open('~.csv', encoding='utf-8') as fp:
    for line in fp:
        if line[0:4] == '"twe':
            continue
        
        uid = line[1:-2].split('","')[1]
        if len(line[1:-2].split('","')) > 20:
            if uid in uid_reuid:
                uid_reuid[uid].append(line[1:-2].split('","')[19])
            else:
                uid_reuid[uid] = [line[1:-2].split('","')[19]]
                
from collections import Counter
re_count_all = dict()
for i in uid_reuid:
    re_count = dict(Counter(uid_reuid[i]))
    if "" in re_count:
        re_count.pop("")
    re_count_all[i] = re_count
    
### G is the network consist of all accounts that has been retweeted    
import networkx as nx
G = nx.DiGraph()

for i in re_count_all:
    for j in re_count_all[i]:
        #dirction A->B means A retweeted B's tweet
        G.add_edge(i,j, weight = re_count_all[i][j])
 
### G1 is the network only made from the IRA network as nodes
import networkx as nx
G1 = nx.DiGraph()

for i in re_count_all:
    for j in re_count_all[i]:
        #dirction A->B means A retweeted B's tweet
        if j in re_count_all.keys():
            G1.add_edge(i,j, weight = re_count_all[i][j])
 
in_degrees = []
out_degrees = []
for i in G1.nodes():
    in_degrees.append(G1.in_degree(i))
    out_degrees.append(G1.out_degree(i))        
 
 plt.hist(in_degrees)
 plt.hist(out_degrees)
 
 density = nx.density(G1)
 print("Network density:", density)
 
from operator import itemgetter
degree_dict = dict(G1.degree(G1.nodes()))
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
print("Top 20 nodes by degree:")
for d in sorted_degree[:20]:
    print(d)
 
        
    
