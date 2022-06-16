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


l = [1,2,3,4,5,6,7]
for i in l:
    print(i)