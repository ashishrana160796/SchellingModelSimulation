# Assigning People Of Two Types to Nodes
# Assign an attribute for this
# Assign 0,1,2 attribute corresponding to (empty, type-1, type-2) 

import networkx as nx
import matplotlib.pyplot as plt
import random

# Size of the grid
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


# display graph function


# list of nodes that will be displayed with particular type of color corresponding to each attribute type 
def display_graph(G):
	nodes_g = nx.draw_networkx_nodes(G,pos, node_color='green', nodelist = type1_node_list)	
	
	nodes_r = nx.draw_networkx_nodes(G,pos, node_color='red', nodelist = type2_node_list)	
	
	nodes_w = nx.draw_networkx_nodes(G,pos, node_color='white', nodelist = empty_cell_list)	
	
	nx.draw_networkx_edges(G,pos)
	nx.draw_networkx_labels(G,pos,labels=labels)
	plt.show()


# for returning a list of boundary nodesin graph

def get_boundary_nodes(G):
	boundary_nodes = []
	for (u,v) in G.nodes():
		if u==0 or u==N-1 or v==0 or v==N-1:
			boundary_nodes.append((u,v))
			# print u,v, 'appended'
			# check the list of appended nodes
	return boundary_nodes



# adding forward and backward diagonal edges in the grid
# data = True is for extracting the value of attribute in later cases


for ((u,v),d) in G.nodes(data=True):
	if(u+1<=N-1) and (v+1<=N-1):
		G.add_edge((u,v),(u+1,v+1))

for ((u,v),d) in G.nodes(data=True):
	if (u+1 <=N-1) and (v-1>=0):
		G.add_edge((u,v),(u+1,v-1))


#plotting the graph 

#nx.draw(G,pos,with_labels=False)
#nx.draw_networkx_labels(G, pos, labels = labels)
#plt.show()				


# assigning the types randomly

for n in G.nodes():
	G.node[n]['type'] = random.randint(0,2)
	


# getting each list of nodes that correspond to each of the attribute type 


empty_cell_list = [n for  (n,d) in G.nodes(data=True) if d['type'] == 0]

type1_node_list = [n for  (n,d) in G.nodes(data=True) if d['type'] == 1]

type2_node_list = [n for  (n,d) in G.nodes(data=True) if d['type'] == 2]

# Checking the respective list of nodes
#print empty_cell_list
#print type1_node_list
#print type2_node_list


# Visualize the graph in two different communities that exist in graph
display_graph(G)
	
	

# Calculate the nodes that unsatisfied i.e. their threshold is not reached till now ...


boundary_nodes = get_boundary_nodes(G) 

internal_nodes = list(set(G.nodes())-set(boundary_nodes))

print boundary_nodes
print internal_nodes



	





