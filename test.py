"""from tkinter import *
import pyautogui
from PIL import ImageTk

root = Tk()
root.geometry("500x500")
root.config()
prompt = '      Press any key      '
label1 = Label(root, text=prompt, width=len(prompt), bg='yellow')
label1.pack()
def key(event):
    if event.char == event.keysym:
        msg = 'Normal Key %r' % event.char
    elif len(event.char) == 1:
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg = 'Special Key %r' % event.keysym
    label1.config(text=msg)
def key1(event):
    # pyautogui.move(50, 50)
    # pyautogui.write('Hello world!', interval=0.25)
    # pyautogui.alert('This is the message to display.')
    # pyautogui.confirm(text='Prueba', title='Titulo', buttons=['OK', 'Cancel'])
    # print(pyautogui.prompt(text='', title='Ingrese txt', default=''))
    # print(pyautogui.password(text='', title='Ingrese pass', default='', mask='*'))
    distance = 225
    while distance > 0:
        pyautogui.drag(distance, 0, duration=0.1)  # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.1)  # move down
        pyautogui.drag(-distance, 0, duration=0.1)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.2)  # move up
def key2(event):
    image1 = pyautogui.screenshot(region=(0, 0, 300, 400))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.pack()
root.bind_all('<Control-Key-c>', key2)
root.mainloop()

class MouseLocation( Frame ):
    def __init__( self, parent ):
        Frame.__init__( self, parent )
        self.parent = parent
        self.initUI()

    def initUI( self ):
        self.parent.title( "Mouse Location" )
        self.pack( fill=BOTH, expand=1 )
        self.mouse_position = StringVar()
        self.mouse_position.set( "X: 0\nY: 0" )
        l = Label( self, textvariable=self.mouse_position, relief=SUNKEN )
        l.pack( fill=X, side=BOTTOM )
        self.bind( "<Motion>", self.update_mouse_position )

    def update_mouse_position( self, event ):
        self.mouse_position.set( "X: %d\nY: %d" % ( event.x, event.y ) )

MouseLocation(root).mainloop()"""

"""arr = [1, 20, 3, 9, 2, 11, 4]
n = len(arr)
sum = 0
i, j = 0, 0

# calculate sum of all elements
for i in range(n):
    sum += arr[i]

if sum % 2 == 0:
    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):

        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
    for i in part:
        print(i)

"""
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edge("a", "b", weight=0.6)
G.add_edge("a", "c", weight=0.2)
G.add_edge("c", "d", weight=0.1)
G.add_edge("c", "e", weight=0.7)
G.add_edge("c", "f", weight=0.9)
G.add_edge("a", "d", weight=0.3)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()