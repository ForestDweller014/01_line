from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = round(x0)
    y0 = round(y0)
    x1 = round(x1)
    y1 = round(y1)
    
    if x1 < x0:
        tempX = x0
        tempY = y0
        x0 = x1
        y0 = y1
        x1 = tempX
        y1 = tempY
    
    deltaX = x1 - x0
    deltaY = y1 - y0
    reflY = 1
    reflSlant = False

    if deltaY < 0:
        #reflect over y = 0 then reflect back again
        y0 *= -1
        
        y1 *= -1

        deltaY *= -1
        
        reflY = -1
    if deltaY > deltaX:
        #reflect over y = x then reflect back again
        temp = x0
        x0 = y0
        y0 = temp
        
        temp = x1
        x1 = y1
        y1 = temp

        temp = deltaX
        deltaX = deltaY
        deltaY = temp

        reflSlant = True
    
    deltaP1 = 2 * (deltaX - deltaY)
    deltaP2 = -2 * deltaY
    p0 = deltaX - 2 * deltaY

    currX = x0
    currY = y0
    if reflSlant:
        temp = currX
        currX = currY
        currY = temp
    currY *= reflY
    plot(screen, color, currX, currY)
    for i in range(deltaX):
        if p0 < 0:
            y0 += 1    
            p0 += deltaP1
        else:
            p0 += deltaP2
        x0 += 1

        currX = x0
        currY = y0
        if reflSlant:
            temp = currX
            currX = currY
            currY = temp
        currY *= reflY
        plot(screen, color, currX, currY)