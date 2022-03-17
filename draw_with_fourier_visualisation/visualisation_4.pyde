from classes import *



state = "draw" #or "show"

drawing = []


time = 0 
path = []


fourierX = []
x = []




def setup():
    size(800,600)
    #global drawing
    #drawing = [PVector(drawing[i][0]-width/2,drawing[i][1]-height/2) for i in range(len(drawing))]
    #setupDraw()
    
    
    
def setupDraw(): 
    global x,fourierX, drawing
    skip = 5
    for i in range(0,len(drawing),skip):
        c = complex(drawing[i].x,drawing[i].y)
        x.append(c)
    
    fourierX = DFT(x)
    toPrint = ''
    for k in range(len(fourierX)):
        toPrint += '(' + str(fourierX[k]['re']) + ' + ' + str(fourierX[k]['im']) + 'i) * (cos(' + str(fourierX[k]['freq']) + 't) - i*sin(' + str(k) +'t)) + ' #e^(-i*t*' + str(fourierX[k]['freq']) + ') + '
    print(toPrint)
    

    
    
def epiCycle(x,y, rota, fourier): #rota ne sert a rien (ca fait tourner le plan)
    for i in range(len(fourier)):
        prevX = x
        prevY = y 
        freq  = fourier[i]['freq']
        rayon = fourier[i]['ampli']
        phase = fourier[i]['phase']
        x += rayon  * cos(freq * time + phase + rota)
        y += rayon  * sin(freq * time + phase + rota)
        
        
        stroke(255,50)
        noFill()
        circle(prevX,prevY,rayon*2)
        fill(255)
        
        stroke(255)
        line(prevX,prevY,x,y)
        stroke(255,100)
        circle(x,y,1)
    return PVector(x,y)




def draw():
    global time, path, fourierX, drawing, state
    background(0)
    
    if state == 'draw': 
        translate(width/2,height/2)
        stroke(255)
        beginShape()
        noFill()
        for i in range(len(drawing)):
            vertex(drawing[i].x, drawing[i].y)
        endShape()
        
    
    elif state == "show" : 
        v = epiCycle(width/2, height/2, 0, fourierX)
        path.insert(0,v)
    
        
        stroke(255,0,0)
        beginShape()
        noFill()
        for i in range(len(path)):
            vertex(path[i].x, path[i].y)
        endShape()
        
        if len(path) == len(fourierX):
            path = []
        
        dt = 2*PI/len(fourierX)
        time += dt





def DFT(x): 
    X = []
    N = len(x)
    for k in range(N):
        sum = complex(0,0)
        for n in range(N):
            IncosAndSin_phi = (2*PI * k * n)/N
            e = complex(cos(-IncosAndSin_phi),sin(-IncosAndSin_phi))
            sum = sum + (x[n] * e) #complexes
        
        sum.re = sum.re/N
        sum.im = sum.im/N
        
        freq  = k
        ampli = sqrt(sum.re**2+sum.im**2) #module
        phase = atan2(sum.im,sum.re)
        X.append({"re" : sum.re, "im" : sum.im, "freq" : freq, "ampli" : ampli, "phase" : phase})
    
    return X

def mousePressed():
    global drawing
    drawing = []
    
def mouseDragged():
    global drawing
    if state == "draw" : 
        drawing.append(PVector(mouseX-width/2,mouseY-height/2))

def keyPressed(): 
    global state
    if key == ENTER:
        state = 'show'
        setupDraw()
        
    
        
    
