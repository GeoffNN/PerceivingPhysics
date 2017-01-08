import numpy as np
import cv2
import csv

ix,iy = -1,-1
# mouse callback function
data = np.zeros((151,2))
compt = 0

def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(255,0,0),-1)
        ix,iy = x,y

# Create a black image, a window and bind the function to window
img = cv2.imread('frame38.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        data[compt,0] = ix
        data[compt,1] = iy
        print ix,iy
        compt += 1


cv2.destroyAllWindows()