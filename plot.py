import numpy as np
import networkx as nx
import string

# now graph
dt = [('len', float)]
a = np.array(ma.getmatrix())

a = a.view()

g_lab ={}

for i in range(len(names)):
    g_lab[i] = str(names[i])

G = nx.from_numpy_matrix(a)
G = nx.relabel_nodes(G, g_lab)


GG = nx.drawing.nx_agraph.to_agraph(G)

GG.node_attr.update(color="red", shape="square")
GG.edge_attr.update(color="blue", width="0.0", arrowhead="none")

GG.draw(outputDir + '/out.png', format='png', prog='dot')