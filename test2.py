import networkx as nx
from matplotlib import pyplot as plt

G = nx.Graph()

# a b c d

G.add_edge('a', 'b', weight=-1.0)
G.add_edge('a', 'c', weight=-2.0)
G.add_edge('b', 'c', weight=-0.1)
G.add_edge('b', 'd', weight=2.0)
G.add_edge('c', 'd', weight=2.0)

"""for (u, v, d) in G.edges(data=True):
    print(u, v, d)"""

# partition = nx.algorithms.community.best_partition(G)
partition = nx.algorithms.community.kernighan_lin.kernighan_lin_bisection(G)

# print(partition)

partition_1, partition_2 = nx.algorithms.community.kernighan_lin_bisection(G)
subgraph_1, subgraph_2 = G.subgraph(partition_1), G.subgraph(partition_2)

# print(partition_1, partition_2)

communities = nx.algorithms.community.girvan_newman(G, most_valuable_edge=None)

node_groups = []
for com in next(communities):
    node_groups.append(list(com))

print(node_groups)
color_map = []
for node in G:
    if node in node_groups[0]:
        color_map.append('blue')
    else:
        color_map.append('green')
nx.draw(G, node_color=color_map, with_labels=True)
plt.show()
