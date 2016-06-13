import turtle
import tkinter
from random import choice, random, seed, randint
from math import cos, floor
import canvasvg

root = tkinter.Tk()
START_WIDTH = 700 
START_HEIGHT = 700 

frame = tkinter.Frame(root, width=START_WIDTH, height=START_HEIGHT)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = tkinter.Scrollbar(frame, orient=tkinter.HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=tkinter.E+tkinter.W)

yscrollbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
yscrollbar.grid(row=0, column=1, sticky=tkinter.N+tkinter.S)

canvas = tkinter.Canvas(frame, width=START_WIDTH, height=START_HEIGHT,
                        scrollregion=(0, 0, START_WIDTH, START_HEIGHT),
                        xscrollcommand=xscrollbar.set,
                        yscrollcommand=yscrollbar.set)

canvas.grid(row=0, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

frame.pack()

t = turtle.RawTurtle(canvas)

class GrowingTree:
    def __init__(self):
        t.tracer(False)        
        self.maxheight = 0
        #left and right
        self.maxwidths = [0,0]
        self.color = [0,0,0]
        t.pencolor(0,0,0)
        #t.colormode(255)
        t.seth(90)
        t.speed(0)
        self.max_possible_height = 0
        self.blength = 0
        self.n_maxbranches = 0
        self.encoding = ''
        t.penup()
        t.setpos(0,-250)
        t.pendown()
        self.height = 0
        self.pensize = 5
        t.pencolor(.5,.5,.5)
        
        #t.tracer(False)
        
        
    def changecolor(self, incv):
        cc = t.pencolor()
        new_c = [cc[i] + incv[i] for i in range(3)]
        for c in new_c:
            c = 255 if c < 255 else c
        t.pencolor(tuple(new_c))
    
    def poll(self):
        temp = t.pos()
        if temp[0] < self.maxwidths[0]:
            self.maxwidths[0] = temp[0]
        elif temp[0] > self.maxwidths[1]:
            self.maxwidths[1] = temp[1]
        if temp[1] > self.maxheight:
            self.maxheight = temp[1]
            #self.changecolor([255/self.height,255/self.height,255/self.height])
    
    def branch(self, angle, length):
        t.right(angle)
        t.forward(length)
        #self.poll()
        t.left(angle)
        self.encoding += '('

    def anglebranch(self, angle, length):
        t.seth(angle)
        t.forward(length)
        #self.poll()
        t.seth(90)
        self.encoding += '('

    def rbranch(self, angle, length):
        t.right(angle)
        t.forward(length)
        #self.poll()
        t.backward(length)
        t.left(angle)
        self.encoding += ')'

    def random_grow(self, n, length):
        self.max_possible_height = (length * cos(45)) * n
        self.blength = length
        self.n_maxbranches = n
        for i in range(n):
            f = self.rbranch if random() < 0.75 else self.branch
            a = choice([-80,-75,-60,-45,45,60,75,80])
            f(a,length)

    def set_height(self,h):
        self.height = h

    def grow(self, encoding, length, spread_factor=3):
        cur_rb = 0
        cur_b = 0
        for e in encoding:
            if e == ')':
                cur_b = 0
                self.rbranch(cur_rb * spread_factor, length)
                cur_rb += 1                
            else:
                cur_rb = 0
                self.branch(cur_b * spread_factor, length)
                cur_b += 1

    def clear(self):
        t.clear()
        t.home()

def compress(enc):
    c = ''
    zerocount = 0
    for e in enc:
        if e == ')':
            zerocount += 1
        else:
            c += str(zerocount) if zerocount > 0 else ''
            c += '('
            zerocount = 0
    return c

'''
def decompres(enc):
    e = ''
    for d in enc:
        if d != '(':
            #problem: might be a multi-digit indicating more than 9 ('s
            e += int(d) * ')'
        else:
            e += d
    return e
'''

class Stack:
    def __init__(self):
        self.l = []
        self.maxdepth = 0
        
    def pop(self):
        if not len(self.l):
            return None
        r = self.l[-1]
        self.l = self.l[:-1]
        return r

    def insert(self, e):
        self.l.append(e)
        if len(self.l) > self.maxdepth:
            self.maxdepth = len(self.l)

    def getmaxdepth(self):
        return self.maxdepth+1

    def size(self):
        return len(self.l)
    
    def __str__(self):
        return str(self.l)

    __repr__ = __str__

def record(tree, angle):
    tree.branch(angle, 10)
    s.insert(angle)

def draw_and_return(enc, length):
    stack = Stack()
    for c in enc:
        if c == "(":
            angle = randint(-30,30)
            stack.insert(angle)
            tree.branch(angle, length)
        else:
            tree.branch(stack.pop()+180,length)
    #t.update()

def next_angle(i, lc, anglerange=180):
    angle = (i+1) * (anglerange/(lc+1))
    return angle

def rec_draw(enc, length=100):
    children = get_children_encodings(enc)
    #print(children)
    lc = len(children)
    if children == []:
        return
    for i in range(lc):
        c = floor(255/tree.height)
        w = t.pensize()
        angle = next_angle(i, lc)
        #tree.changecolor([c,0,c])
        t.pensize(w*.9)
        tree.anglebranch(angle, length-(length/tree.height))        
        rec_draw(children[i][1:-1],length-(length/tree.height))
        t.penup()
        #tree.changecolor([-c,0,-c])
        t.pensize(w)
        tree.anglebranch(180+angle, length-(length/tree.height))
        t.pendown()
    #t.update()

def generate_random_encoding(max_tries):
    r = ''
    s = Stack()
    for i in range(max_tries):
        if (choice(["(", ")"]) == "("):
            s.insert(i)
            r += "("
        else:
            if s.pop():
                r += ")"
    '''while s.size():
        if (choice(["(", ")"]) == "("):
            s.insert(i)
            r += "("
        else:
            if s.pop():
                r += ")"'''
    while True:
        if s.pop():
            r += ")"
        else:
            if len(r) % 2 == 1:
                r+=")"
            break
    return (r,s.getmaxdepth())

def get_children_encodings(penc):
    if penc == '':
        return []
    s = Stack()
    childbuf = ''
    children = []
    for e in penc:
        if e == "(":
            s.insert(e)
            childbuf += e
        else:
            s.pop()
            childbuf += e
            if s.size() == 0:
                children.append(childbuf)
                childbuf = ''
    return children

if __name__ == "__main__":
    tree = GrowingTree()
    #tree.random_grow(100,5)
    #e = tree.encoding
    enc,height = generate_random_encoding(1000)
    tree.set_height(height)
    rec_draw(enc)
    #t.tracer(True)
    #tree.random_grow(100, 50)
    canvas.config(scrollregion=canvas.bbox(tkinter.ALL))
    canvas.postscript(file="test.eps")
    saveall("test.svg", canvas)
    
