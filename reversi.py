#starting othelo from scratch


import tkinter
from tkinter import *
import random
from collections import OrderedDict

#init colors
b = '#000000'
w = '#ffffff'
s = '#65b0f2'
o = '#81c8f4'

#create tkinter interface
root = tkinter.Tk()
root.wm_title('Othello')
root.configure(background=o, cursor="none")

#creates space on gui for game board
canvas = tkinter.Canvas(root, height=410, width=410, background='#999999')
canvas.grid(row=0, column=0, rowspan = 4, columnspan = 4)
canvas.pack

#creates space on gui for instructions
inst = tkinter.Label(root, bg = o, font =('Tempus Sans ITC', 10, 'bold'),text='add instructions here')
inst.grid(row = 0, column = 5)

#defines some variables
size = 6 #how many game spaces are in a row
d = 410/size #size of one game space (change if board size changes)
turn = 2 #turn counter (accumulator)

#loop to create the cells for game spaces - fix terms!
for colum in range(1,size+1): #the first column is 1, more logic than 0
        cob = colum - 1 
        for cells in range(1,size+1):
            cev = cells + (6*cob)
            ceb = cells - 1
            startx = cells + (d*ceb)
            starty = colum + (d*cob)
            mat = [colum,ceb+1, cev]
            #print(str(mat))
            new_cell = canvas.create_polygon(startx, starty,  startx+d,starty,  startx+d, starty+d, startx, starty+d, 
                                fill = s, outline = '#000000', tags = (mat[0],mat[1],mat[2]))

#sets the place for the starter pawns 
circles = ['15','16','22','21']
starts = [canvas.find_withtag(circles[0]),canvas.find_withtag(circles[1]),
          canvas.find_withtag(circles[2]),canvas.find_withtag(circles[3])]

#creates the starter pawns - can be simplified? 
t = 0
for start in starts:
    global t
    global starts
    coordz = canvas.coords(start)
    b1 = coordz[0] + size
    b2 = coordz[1] + size
    b3 = coordz[4] - size
    b4 = coordz[5] - size
    lo = circles[t]+'c'
    if t % 2 == 0:
        newpawn = canvas.create_oval(b1,b2,b3,b4, outline = w, fill = w,
                                     tags = ('w', lo))
        #print(canvas.gettags(newpawn))
    else:
        newpawn = canvas.create_oval(b1,b2,b3,b4, fill = b, tags = ('b', lo))
        #print(canvas.gettags(newpawn))
    t = t+1

#adds a new pawn where clicked if able to score, changes sandwiched colors
def click(event):
    global turn
    global side
    tu = False
    coordz = canvas.coords(canvas.find_withtag(CURRENT))
    b1 = coordz[0] + size
    b2 = coordz[1] + size
    b3 = coordz[4] - size
    b4 = coordz[5] - size
    flags = canvas.gettags(canvas.find_withtag(CURRENT))
    print(flags)
    pos = flags[2]
    row = flags[0]
    column = flags[1]
    #diagonals loop
    vert1 = []
    vert2 = []
    v1, v2, v3, v4 = int(pos),int(pos),int(pos),int(pos)
    edges = [1,2,3,4,5,6,7,12,13,18,19,24,25,30,31,32,33,34,35,36]
    while True:
        v1 = v1 - (size + 1)
        if v1 <= 0:
            break
        vert1.append(v1)
    while True:
        v2 = v2 + (size + 1)
        if v2 >= 37:
            break
        vert1.append(v2)
        if v2 in edges:
            break
        vert1.append(v2)
    while True:
        v3 = v3 - (size - 1)
        if v3 <= 0:
            break
        vert2.append(v3)
    while True:
        v4 = v4 + (size - 1)
        if v4 >= 36:
            break
        vert2.append(v4)
        if v4 in edges:
            break
        vert2.append(v4)
    diag1 = list(OrderedDict.fromkeys(vert1))
    diag2 = list(OrderedDict.fromkeys(vert2))
    #print(diag1)
    #print(diag2)
    #so, our program so far can tell every game space in available path
    #close = [diag1[0], diag1[1],diag2[0],diag1[1],]
    pattern = [ +1, -1, +size, -size, +(size+1), -(size+1), +(size-1), -(size-1)]
    hits = []
    ends = []
    if turn % 2 == 0:
        opp = 'w'
        same = 'b'
        f = b
    if turn % 2 != 0:
        opp = 'b'
        same = 'w'
        f = w
    for options in range(len(pattern)):
        checking = int(pos)+pattern[options] #find touching cells
            #print(checking)
        if opp in canvas.gettags(canvas.find_withtag(str(checking)+'c')): #oposite color?
            hits.append(checking)
            checking = checking + pattern[options]
            if checking in edges:
                break
            if same in canvas.gettags(canvas.find_withtag(str(checking)+'c')): #same color?
                ends.append(checking)
            if opp in canvas.gettags(canvas.find_withtag(str(checking)+'c')):
                hits.append(checking)
                checking = checking + pattern[options]
                if checking in edges:
                    break
                if same in canvas.gettags(canvas.find_withtag(str(checking)+'c')): #same color?
                    ends.append(checking)
                if opp in canvas.gettags(canvas.find_withtag(str(checking)+'c')):
                    hits.append(checking)
                    checking = checking + pattern[options]
                    if checking in edges:
                        break
                    if same in canvas.gettags(canvas.find_withtag(str(checking)+'c')): #same color?
                        ends.append(checking)
                    if opp in canvas.gettags(canvas.find_withtag(str(checking)+'c')):
                        hits.append(checking)
                        checking = checking + pattern[options]
                        if checking in edges:
                            break
                        if same in canvas.gettags(canvas.find_withtag(str(checking)+'c')): #same color?
                            ends.append(checking)
            if len(ends) >= 1:
                newpawn = canvas.create_oval(b1,b2,b3,b4, fill = f, outline = f,
                                     tags = (same,  (str(pos)+'c')))
                for scores in range(len(hits)):
                    change = str(hits[scores])+'c'
                    canvas.itemconfig(change,fill = f, outline = f, tags = (change,same))
                tu = True
                        
                        
    if tu == True:
        turn = turn +1
    print(turn)
    print(hits)
    print(ends)
    
    #now to check if scoring (reverse color)
    #place pawn
    #change colors in between
    #change pawn color
    
    
#scoring


#binds the event of the button being clicked to the thing called click
canvas.bind("<Button-1>", click)

root.mainloop()
