import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

root = tkinter.Tk()

fig = plt.Figure()
#sub = fig.add_subplot('111')

canvas = FigureCanvasTkAgg(fig, master=root)
#canvas.draw()
canvas.get_tk_widget().pack() #fill='both', expand=True)

G = nx.Graph()

G.add_edge("a", "b", weight=0.6)
G.add_edge("a", "c", weight=0.2)
G.add_edge("c", "d", weight=0.1)
G.add_edge("c", "e", weight=0.7)
G.add_edge("c", "f", weight=0.9)
G.add_edge("a", "d", weight=0.3)


pos = nx.spring_layout(G)  # positions for all nodes - seed for reproducibility

# nodes
ax = fig.gca()  # it can gives list of `ax` if there is more subplots.
nx.draw_networkx(G, ax=ax, pos=pos, arrows=True)
nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"))

tkinter.mainloop()