import cv2 as cv
import numpy as np
import time
import math
  
vid = cv.VideoCapture(1, cv.CAP_DSHOW)

while True:

    ret, frame = vid.read()
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
  
while(True):
    
    count = 1
    while (count > 0):
        print(count)
        count = count - 1
        time.sleep(1)
        
    ret, img = vid.read()
    if cv.waitKey(0):
        break
  

vid.release()

cv.destroyAllWindows()

def FrameFit (frame, scale=1):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)
        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#cv.imshow('chessboard',img)

Fit = FrameFit(img)
hough = np.copy(Fit)
shape = np.copy(Fit)
cv.imshow('fit', Fit)

blur = cv.GaussianBlur(Fit, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny', canny)

gry = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
gry = np.float32(gry)

corner = cv.cornerHarris(gry, 5, 3, 0.04)
#cv.imshow('Corner', corner)

lines = cv.HoughLines(canny, 1, np.pi / 180, 150, None, 0, 0)
if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(hough, pt1, pt2, (255,0,0), 2, cv.LINE_AA)

Grid = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
Grid[corner>0.005 * corner.max()] = [0,0,255]
#cv.imshow('Grid', Grid)

mask = cv.bitwise_or(Grid, hough)
cv.imshow('Mask',mask)

cv.waitKey(0)
