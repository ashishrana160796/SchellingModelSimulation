# Base code 
# For building the structure of the grid in consideration

import networkx as nx
import matplotlib.pyplot as plt

N = 10

# Getting grid graph of dimension N*N
G = nx.grid_2d_graph(N,N)

# For proper ordering of nodes in 2-D grid shape
pos = dict( (n,n) for n in G.nodes() )

# for proper label assignment of nodes in grid
labels = dict( ((i,j),i*10+j) for i,j in G.nodes() )

# General Feature Of Graphs
# i here represents columns
# j  here represents rows


# adding forward and backward diagonal edges in the grid

for ((u,v),d) in G.nodes(data=True):
	if(u+1<=N-1) and (v+1<=N-1):
		G.add_edge((u,v),(u+1,v+1))

for ((u,v),d) in G.nodes(data=True):
	if (u+1 <=N-1) and (v-1>=0):
		G.add_edge((u,v),(u+1,v-1))


#plotting the graph 

nx.draw(G,pos,with_labels=False)
nx.draw_networkx_labels(G, pos, labels = labels)
plt.show()				
