from graph import *

# (230,230,230) - grey color
# (0,255,255) - sky color
# (170,255,255) - sun color
# (230,230,230) - bear color

def dog(x,y,k,m) :
    penSize(k)
    #dog's body
    elips(x,y,45*k,30*k,  (108,103,83))
    elips(x+54*m*k,y-13*k,25*k,19*k,  (108,103,83))
    elips(x+34*m*k,y-20*k,13*k,12*k,  (108,103,83))
    elips(x+10*m*k,y+43*k,15*k,30*k,  (108,103,83))
    elips(x-40*m*k,y+30*k,15*k,30*k,  (108,103,83))
    elips(x+70*k*m,y+3*k,15*k,20*k,  (108,103,83))
    elips(x+82*m*k,y+30*k,5*k,20*k,  (108,103,83))
    elips(x+46*m*k,y+15*k,5*k,20*k,  (108,103,83))
    elips(x-43*m*k,y+62*k,14*k,6*k,  (108,103,83))
    elips(x+5*m*k,y+75*k,14*k,6*k,  (108,103,83))
    elips(x+42*m*k,y+35*k,10*k,4*k,  (108,103,83))
    elips(x+79*m*k,y+49*k,10*k,4*k,  (108,103,83))

    #dog's head (90 460)
    brushColor(108,103,83)
    rectangle(x-47*m*k,y-45*k,x+10*k*m,y+16*k)
    circle(x+8*k*m,y-34*k,10*k)
    circle(x-47*k*m,y-34*k,10*k)
    elips(x-30*m*k,y-27*k,5*k,2*k,  (255,255,255))
    elips(x-10*m*k,y-27*k,5*k,2*k,  (255,255,255))
    contur_elips(x-30*m*k,y-27*k, 6*k, 2*k)
    contur_elips(x-10*k*m,y-27*k, 6*k, 2*k)
    brushColor(0,0,0)
    circle(x-30*m*k,y-27*k,2*k)
    circle(x-10*m*k,y-27*k,2*k)
    points = [x-37*m*k,y+8*k],[x-35*m*k,y+4*k],[x-31*m*k,y], [x-24*m*k,y-2*k],[x-18*m*k,y-2*k],[x-11*m*k,y],[x-6*k*m,y+4*k],[x-4*m*k,y+8*k]     
    polyline(points)
    brushColor(255,255,255)
    polygon([ (x-35*k*m,y+4*k), (x-31*m*k,y),(x-33*m*k,y-6*k)])
    polygon([ (x-6*k*m,y+4*k), (x-11*k*m,y),(x-7*m*k,y-6*k)])


def elipsfill(x,y, x0, y0, a, b)  :
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1):
        return True
    else :
        return False
    
def elipsboard (x,y, x0, y0, a, b):
    e = 0.2
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1+e
         and
         (x-x0)**2/(a**2) + (y-y0)**2/(b**2) >= 1-e) :
        return True
    else :
        return False
    
def contur_elips(x0,y0, a, b):
    for x in range(int(x0-a),int(x0+a)):
        for  y in range(int(y0-b),int(y0+b)):
            if elipsboard (x,y, x0, y0, a, b):
                 point (x,y,"black")        
                 
def elips(x0, y0, a, b, color):
    for x in range(int(x0-a),int(x0+a)):
        for  y in range(int(y0-b),int(y0+b)):
            if elipsfill(x,y, x0, y0, a, b):
                point(x,y,color)

windowSize(420,600)
canvasSize(420,600)
brushColor(159,199,247)
rectangle(0, 0, 420, 147)
#brushColor(200,171,55)
#rectangle(0, 90, 420, 340 )
brushColor(55,200,113)
rectangle(0, 287, 420, 600)

#fence1
brushColor(200,171,55)
rectangle(82, 7, 420, 214)
for i in range(12):
    line(109+i*28,7, 109+i*28,215)

#fence2
brushColor(200,171,55)
rectangle(0, 147, 230, 286)
for i in range(12):
    line(0+i*20,147, 0+i*20,286)

#fence3
brushColor(200,171,55)
rectangle(209, 214, 420, 355)
for i in range(15):
    line(208+i*16,214, 208+i*16,355)

#fence4
brushColor(200,171,55)
rectangle(0, 231, 193, 370)
for i in range(10):
    line(0+i*20,231, 0+i*20,370)

dog(385,361,0.7,-1)
#doghouse
brushColor(200,171,55)
polygon([(340, 480), (340,380), (270,360), (270,450)])
polygon([(340, 480), (340,380), (365,360), (365,435)])
brushColor(212,160,0)
polygon([ (340,380), (270,360), (310,315)])
polygon([ (340,380), (365,360),(335,300), (310,315)])
elips(305,415,20,25,  (0,0,0))

#chain
for i in range(10):
    contur_elips(285-i*5,435+i*5, 5+7*(i%2),5+7*((i+1)%2) )
for j in range(3):
    contur_elips(235-j*6,475+j*3, 5+7*(j%2),5+7*((j+1)%2) )
contur_elips(200,480, 20, 10)

dog(78,370,1,1)
dog(118,512,1,-1)
dog(380,555,2.5,1)
run()

