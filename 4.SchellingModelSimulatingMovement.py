# Main Task Of This Code
# Getting a list of nodes that are unsatisfied


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
	for ((u,v),d) in G.nodes(data=True):
		if u==0 or u==N-1 or v==0 or v==N-1:
			boundary_nodes.append((u,v))
			# print u,v, 'appended'
			# check the list of appended nodes
	return boundary_nodes



# methods returning the neighbours of a given node

def get_neigh_node_internal(u,v):
	
	return [(u-1,v-1),(u,v-1),(u+1,v-1),(u-1,v),(u+1,v),(u-1,v+1),(u,v+1),(u+1,v+1)]


def get_neigh_node_external(u,v):

	if u==0 and v==0 :
		return [(0,1),(1,1),(1,0)]
	elif u==N-1 and v==N-1 :
		return [(N-2,N-2),(N-1,N-2),(N-2,N-1)]
	elif u==N-1 and v==0:
		return [(u-1,v),(u,v+1),(u-1,v+1)]
	elif u==0 and v == N-1:
		return [(u+1,v),(u,v-1),(u+1,v-1)]	
	elif u==0:
		return [(u,v-1),(u,v+1),(u+1,v),(u+1,v-1),(u+1,v+1)]
	elif u==N-1:
		return [(u,v-1),(u,v+1),(u-1,v),(u-1,v-1),(u-1,v+1)]
	elif  v==N-1:	
		return [(u-1,v),(u+1,v),(u-1,v-1),(u,v-1),(u+1,v-1)]
	elif v==0:
		return [(u-1,v),(u+1,v),(u,v+1),(u-1,v+1),(u+1,v+1)]
							


def get_unsatisfied_nodes(G, boundary_nodes, internal_nodes):
	
	unsatisfied_nodes = []
	threshold = 3
	
	for u,v in G.nodes():
		type_of_node = G.node[(u,v)]['type']
		
		if type_of_node == 0:
			continue
		else :
			similar_nodes = 0
			
			if (u,v) in internal_nodes:
				neigh = get_neigh_node_internal(u,v)
			elif (u,v) in boundary_nodes: 			
				neigh = get_neigh_node_external(u,v)
						
			for each in neigh:
				if (G.node[each]['type'] == type_of_node):
					similar_nodes = similar_nodes+1
				
			if similar_nodes <= threshold: 
				unsatisfied_nodes.append((u,v))		
	
	return unsatisfied_nodes
	

# movement of node such that it becomes satisfied

def make_node_satisfied(unsatisfied_nodes, empty_cell_list):
	if len(unsatisfied_nodes) != 0:
		shift_node = random.choice(unsatisfied_nodes)
		new_pos = random.choice(empty_cell_list)
		
		# types are interchanged
		G.node[new_pos]['type'] = G.node[shift_node]['type']
		G.node[shift_node]['type'] = 0
		
		labels[shift_node],labels[new_pos] = labels[new_pos],labels[shift_node]
	
	else:
		pass
			

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
unsatisfied_nodes = get_unsatisfied_nodes(G, boundary_nodes, internal_nodes)



#print boundary_nodes
#print internal_nodes

# Iteration limited because for higher threshold values and empty cell being present the loop might never reach an end
for i in range(10000):
	unsatisfied_nodes = get_unsatisfied_nodes(G, boundary_nodes, internal_nodes)
#print unsatisfied_nodes
	make_node_satisfied(unsatisfied_nodes, empty_cell_list)
	
	empty_cell_list = [n for (n,d) in G.nodes(data=True) if d['type'] == 0]
	type1_node_list = [n for (n,d) in G.nodes(data=True) if d['type'] == 1]
	type2_node_list = [n for (n,d) in G.nodes(data=True) if d['type'] == 2]

#make_node_satisfied(unsatisfied_nodes, empty_cell_list)
	
display_graph(G)	





