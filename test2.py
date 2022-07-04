"""from tkinter import ttk

import networkx as nx
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

G = nx.Graph()

# a b c d

G.add_edge('a', 'b', weight=-1.0)
G.add_edge('a', 'c', weight=-2.0)
G.add_edge('b', 'c', weight=-0.1)
G.add_edge('b', 'd', weight=2.0)
G.add_edge('c', 'd', weight=2.0)


# partition = nx.algorithms.community.best_partition(G)
partition = nx.algorithms.community.kernighan_lin.kernighan_lin_bisection(G)

# print(partition)

partition_1, partition_2 = nx.algorithms.community.kernighan_lin_bisection(G)
subgraph_1, subgraph_2 = G.subgraph(partition_1), G.subgraph(partition_2)

root = tk.Tk()
root.title("Grafo")
root.background = "#eafff5"
print(type(subgraph_1))
frameFigure = ttk.Frame(root)
frameFigure.grid(row=0, column=1, rowspan=4)

figure = plt.figure(frameon=True, figsize=(7, 5), dpi=100)
canvas = FigureCanvasTkAgg(figure, master=frameFigure)

figure.set_facecolor('#eafff5')
plt.axis('off')
communities = nx.algorithms.community.girvan_newman(G, most_valuable_edge=None)

node_groups = []
for com in next(communities):
    node_groups.append(list(com))

print(node_groups)
color_map = []
for node in G:
    if node in node_groups[0]:
        color_map.append('#44e011')
    else:
        color_map.append('#bb85f0')
pos = nx.spring_layout(G, 25)
nx.draw_networkx(G, pos=pos, node_color=color_map, alpha=0.9, edge_color='green')
nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))

canvas.draw()
canvas.get_tk_widget().pack()
root.mainloop()
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge('a', 'b', weight=1.0)
G.add_edge('a', 'c', weight=2.0)
G.add_edge('b', 'c', weight=3.0)
G.add_edge('b', 'd', weight=4.0)
G.add_edge('c', 'd', weight=5.0)

def create_partition(graph):
    partition_1, partition_2 = nx.algorithms.community.kernighan_lin_bisection(graph)
    print(partition_1)
create_partition(G)
