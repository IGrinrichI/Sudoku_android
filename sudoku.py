#-*-coding:utf8;-*-
#qpy:console
import time
from math import sqrt
size = 9
sqrsize = int(sqrt(size))
figures = []
digon = False

def show(f):
    s = ""
    jj = 0
    for row in f:
        j = 0
        jj += 1
        for i in row:
            j += 1
            s += str(i) + " "
            if j % sqrsize == 0:
                s += " "
        s += "\n"
        if jj % sqrsize == 0:
            s += "\n"
    print(s)
    
def combine(f,fcnc):
    chet = False
    outcombine = ""
    for i in range(len(f)):
        if f[i] != "." and fcnc[i] == "*":
            if int(f[i]) % 2 == 0:
                chet = True
            break
    
    for i in range(len(f)):
        if f[i] == "." and fcnc[i] == "*":
            outcombine += "+" if chet else "-"
        else:
            outcombine += f[i]
    return outcombine
    
def tomtrx(n,f1):
    f = [[0 for i in range(size)] for j in range(size)]
    for i in range(size*size):
        if n[i] == "+":
            f[i//size][i%size] = 0
            for j in range(size):
                if j % 2 == 0:
                    f1[i//size][i%size][j] = 0
        elif n[i] == "-":
            f[i//size][i%size] = 0
            for j in range(size):
                if j % 2 == 1:
                    f1[i//size][i%size][j] = 0
        elif n[i] == ".":
            f[i//size][i%size] = 0
        else:
            f[i//size][i%size] = int(n[i])
    return f

def createcol():
    f = []
    for i in range(size):
        fig = []
        for j in range(size):
            fig.append([i, j])
        f.append(fig)
    return f
    
def createrow():
    f = []
    for i in range(size):
        fig = []
        for j in range(size):
            fig.append([j, i])
        f.append(fig)
    return f
    
def createsqr():
    f = []
    for i in range(size):
        sx = (i % sqrsize) * sqrsize
        sy = (i // sqrsize) * sqrsize
        fig = []
        for j in range(size):
            fig.append([sx + j % sqrsize, sy + j // sqrsize])
        f.append(fig)
    return f
    
def createdig():
    f = []
    for i in range(2):
        fig = []
        if i == 0:
            for j in range(size):
                fig.append([j, j])
        else:
            for j in range(size):
                fig.append([j, size - j - 1])
        f.append(fig)
    return f

def addmin(mins,coord,num):
    if not mins.__contains__([coord,num]):
        mins.append([coord,num])

def search(f1):
    mins = []
    
    for fig in figures:
        figsum = [0 for i in range(size)]
        for coord in fig:
            if sum(f1[coord[1]][coord[0]])==1:
                addmin(mins,coord,f1[coord[1]][coord[0]].index(1)+1)
            for i in range(size):
                figsum[i] += f1[coord[1]][coord[0]][i]
        if figsum.__contains__(1):
            indx = figsum.index(1)
            for coord in fig:
                if f1[coord[1]][coord[0]][indx] == 1:
                    addmin(mins,coord,indx+1)
                    break
    return mins

def predict(f,f1,v,x,y):
    f[y][x] = v
    f1[y][x] = [0 for i in range(size)]
    index = v-1
    for fig in figures:
        if fig.__contains__([x,y]):
            for coord in fig:
                f1[coord[1]][coord[0]][index] = 0
    
def solver(f,f1):
    mins = search(f1)
    if len(mins) > 0:
        for m in mins:
            predict(f,f1,m[1],m[0][0],m[0][1])
        return solver(f,f1)
    else:
        figures = []
        return f
    
def solve(n):
    f1 = [[[1 for i in range(size)] for j in range(size)] for k in range(size)]
    f = tomtrx(n,f1)
    for y in range(size):
        for x in range(size):
            if f[y][x] != 0:
                predict(f,f1,f[y][x],x,y)
    return solver(f,f1)


def complect():
    figures.extend(createcol())
    figures.extend(createrow())
    figures.extend(createsqr())
    if digon:
        figures.extend(createdig())






n1 = "1..+.5..6.+.........98.+1+.+.3..........+783+2.+.6......4.5.+.9..+.7..+25...+.37+"
n2 = "...6.5-...-..7.9.......-.1-4..72.-.9.7.5.6.8.8.-.13..5-2.-.......8.6..-...-3.1..."
n3 = ".........4...6...9.85.1.43..-.1.9.-..-..7..-..-.4.2.-..12.9.35.6...5...8........."
n4 = "5.-...-.7...6.5...-..7.9..-.27...58.....5.....65...39.-..5.8..-...1.3...7.-...-.3"

nm = "..........72.6.1....51...82.8...13..4.........37.9..1.....238..5.4..9.........79."

nn = ("..4"+"37."+"19."+
      "..2"+"..."+"7.."+
	  ".3."+"2.-"+".5."+
	     		
	  ".-."+".5."+"..-"+
      "..."+"..."+"..."+
	  "-.."+".9."+".-."+
	     		
	  ".5."+"-.9"+".2."+
      "..3"+"..."+"4.."+
	  ".87"+".62"+"3.."
)
n5 = "+93+5.78+5+.+..++92.+.++..5++.3+9+..3.+..++.2.+.5+6.+.9.+.+..+87+++....6+15+9+47."
n7 = "....3.......5.8...5..4.2..8.17...52.2.......4.48...31.9..8.5..3...9.3.......4...."
n8 = ".67......5..2.9...1..5......42....7...........3....82......1..3...4.7..6......25."
n9 = "..5...6.....7.6...3.......7.6..2..4....4.3....3..8..5.2.......9...3.4.....9...5.."
n10= ".......6....74...8.....2....3..9.1...6.3.8.2...8.6..4....6.....3...71....2......."

#t = time.time()
#show(solve(n10))
#print(time.time() - t)