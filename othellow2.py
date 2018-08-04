#Othello! also called Reversi
#in this version it knows the cell numbs of cells in its colummn or row when you click
#and will only set a pawn if there is a pawn of the same color in that coulmn or row already
#however the last cell 36 does not work

import tkinter
from tkinter import *
import random

#init colors
b = '#000000'
w = '#ffffff'
s = '#65b0f2'
o = '#81c8f4'

root = tkinter.Tk()
root.wm_title('Othello')
root.configure(background=o, cursor="none")

canvas = tkinter.Canvas(root, height=410, width=410, background='#999999')
canvas.grid(row=0, column=0, rowspan = 4, columnspan = 4)
canvas.pack

inst = tkinter.Label(root, bg = o, font =('Tempus Sans ITC', 10, 'bold'),text='add instructions here')
inst.grid(row = 0, column = 5)

size = 6
d = 410/size
turn = 2
r = 6

for colum in range(1,size+1):
        cob = colum - 1
        for cells in range(1,size+1):
            cev = cells + (6*cob)
            ceb = cells - 1
            startx = cells + (d*ceb)
            starty = colum + (d*cob)
            new_cell = canvas.create_polygon(startx, starty,  startx+d,starty,  startx+d, starty+d, startx, starty+d, 
                                fill = s, outline = '#000000', tags = (str(cev)))

#init 4 center circles
circles = ['15','16','22','21']
starts = [canvas.find_withtag(circles[0]),canvas.find_withtag(circles[1]),
          canvas.find_withtag(circles[2]),canvas.find_withtag(circles[3])]
t = 0
for start in starts:
    global t
    global starts
    coordz = canvas.coords(start)
    b1 = coordz[0] + r
    b2 = coordz[1] + r
    b3 = coordz[4] - r
    b4 = coordz[5] - r
    lo = circles[t]+'c'
    if t % 2 == 0:
        newpawn = canvas.create_oval(b1,b2,b3,b4, outline = w, fill = w,
                                     tags = ('w', lo))
        print(canvas.gettags(newpawn))
    else:
        newpawn = canvas.create_oval(b1,b2,b3,b4, fill = b, tags = ('b', lo))
        print(canvas.gettags(newpawn))
    t = t+1
            
def click(event):
    global turn
    global side
    tu = False
    coordz = canvas.coords(canvas.find_withtag(CURRENT))
    b1 = coordz[0] + r
    b2 = coordz[1] + r
    b3 = coordz[4] - r
    b4 = coordz[5] - r
    flags = canvas.gettags(canvas.find_withtag(CURRENT))
    pos = flags[0]
    print('position = ' + pos)
    row = [0, size, size*2, size*3, size*4, size*5, size*6]
    vert = []
    v1, v2 = int(pos),int(pos)
    a1, a2 = int(pos),int(pos)
    #calculating the cells in a column
    while True:
        v1 = v1 - size
        if v1 <= 0:
            break
        vert.append(v1)
    while True:
        v2 = v2 + size
        if v2 >= 36:
            break
        vert.append(v2)
    #print(vert)
    #calculating cell numbers in a row
    across = []
    while True:
        a1 = a1 - 1
        #print(a1)
        if a1 in row:
            break
        across.append(a1)
    if int(pos) not in row:
        while True:
            a2 = a2 + 1
            across.append(a2)
            if a2 in row:
                break
    #print(across)  
    path = vert + across
    print(path)
        
    if turn % 2 == 0:
        for cells in range(len(path)):
            ce = str(path[cells])+'c'
            #print(ce)
            #print(canvas.gettags(canvas.find_withtag(ce)))
            if 'w' in canvas.gettags(canvas.find_withtag(ce)):
                #print('true1')
                nc = str(pos)+'c'
                newpawn = canvas.create_oval(b1,b2,b3,b4, outline = w, fill = w,
                                     tags = ('w',  nc))
                tu = True
    if turn % 2 != 0:
        for cells in range(len(path)):
            ce = str(path[cells])+'c'
            #print(ce)
            #print(canvas.gettags(canvas.find_withtag(ce)))
            if 'b' in canvas.gettags(canvas.find_withtag(ce)):
                #print('true2')
                nc = str(pos)+'c'
                newpawn = canvas.create_oval(b1,b2,b3,b4, fill = b,
                                     tags = ('b',  nc))
                tu = True
    if tu == True:
        turn = turn +1
        print(turn)
        #print(canvas.gettags(newpawn))
    bpawns = 0
    wpawns = 0   
    if turn == 8:
        for turnz in range(1,37):
            cel = str(turnz)+'c'
            #print(cel)
            if 'b' in canvas.gettags(canvas.find_withtag(cel)):
                bpawns = bpawns + 1
                print(bpawns)
            if 'w' in canvas.gettags(canvas.find_withtag(cel)):
                wpawns = wpawns + 1
                print(wpawns)
        print('black pawns = ' + str(bpawns))
        print('white pawns = ' + str(wpawns))

canvas.bind("<Button-1>", click)

root.mainloop()