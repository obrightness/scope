import serial
import signal
import numpy as np
import pygame
import sys
ser = serial.Serial('/dev/ttyUSB0', 9600)
screen = pygame.display.set_mode((960, 720))
screen.fill((255, 255, 255))

#plt.ion() # set plot to animated

def handler(a, b):
    signal.pause()
    print "handler"
def handler2(a, b):
    print "gO!"
def handleStop(a, b):
    sys.exit();

signal.signal(signal.SIGTSTP, handler)
signal.signal(signal.SIGQUIT, handler2)
signal.signal(signal.SIGTERM, handleStop )
x_range = 500
ydata = [0] * x_range 
#ax1=plt.axes()  

# make plot
#line, = plt.plot(ydata)
#plt.ylim([10,40])

def plot(x, y, xmin, xmax, ymin, ymax, pygame_screen):
    w, h = pygame_screen.get_size()
    x = np.array(x)
    y = np.array(y)

    #Scale data
    xspan = abs(xmax-xmin)
    yspan = abs(ymax-ymin)
    xsc = 1.0*w/xspan
    ysc = 1.0*h/yspan
    xp = (x-xmin)*xsc
    yp = h-(y-ymin)*ysc
    pygame_screen.fill((255,255,255))
    #Draw grid
    grid_color = (210, 210, 210)
    for i in range(10):
        pygame.draw.line(pygame_screen, grid_color, (0,int(h*0.1*i)), (w-1,int(h*0.1*i)), 1)
        pygame.draw.line(pygame_screen, grid_color, (int(w*0.1*i),0), (int(w*0.1*i),h-1), 1)

    #Plot data
    for i in range(len(xp)-1):
        pygame.draw.line(pygame_screen, (0, 0, 255), (int(xp[i]), int(yp[i])), (int(xp[i+1]), int(yp[i+1])), 1)


# start data collection
while True:
    try:
        data = ser.readline().rstrip() # read data from serial 
    except:
        print "except"
        continue
    if len(data) > 5:
        print data
        continue;
    x = np.arange(x_range) 
    try:
        ydata.append(float(data))
    except:
        print data
        continue 
    del ydata[0]
    plot(x, ydata, 0, x_range, 0, 700, screen)
    pygame.display.flip()
'''
while True:  
    data = ser.readline().rstrip() # read data from serial 
    #print data
    # port and strip line endings
    #if len(data.split(".")) == 2:
    if len(data) > 5:
        continue;
    ymin = float(min(ydata))-10
    ymax = float(max(ydata))+10
    plt.ylim([0,32767])
    ydata.append(float(data))
    del ydata[0]
    line.set_xdata(np.arange(len(ydata)))
    line.set_ydata(ydata)  # update the data
    plt.draw() # update the plot
'''
