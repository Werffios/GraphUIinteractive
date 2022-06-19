import psutil
import tkinter as tk
from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

root = Tk()
root.title("Hello")

fig = plt.figure(frameon=True, figsize=(5, 1), dpi=100)
canvas = FigureCanvasTkAgg(fig, root)
Node = nx.Graph()

Node.add_edge("a", "b", weight=0.6)
Node.add_edge("a", "c", weight=0.2)
Node.add_edge("c", "d", weight=0.1)
Node.add_edge("c", "e", weight=0.7)
Node.add_edge("c", "f", weight=0.9)
Node.add_edge("a", "d", weight=0.3)

plt.gca().set_facecolor("grey")
fig.set_facecolor("black")
pos = nx.spring_layout(Node, 25)
nx.draw_networkx(Node, pos=pos, alpha=1,
                 with_labels=False, node_size=100, node_color="green")
nx.draw_networkx_edge_labels(Node, pos, nx.get_edge_attributes(Node, "weight") )

canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)


root.mainloop()
