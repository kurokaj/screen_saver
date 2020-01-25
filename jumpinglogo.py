import numpy as np
import cv2
import math

#***********************************************************

def new_position(x,y,v_x, v_y):

    s_x = x + v_x
    s_y = y + v_y

    return (s_x ,s_y)


#***********************************************************

path_fore = "/home/jonne/back_up/PROJEKTIT/Screensaver/eme.png" # Path to the bouncing image
bounce = cv2.imread(path_fore,1)
scale_percent = 10
aw = int(bounce.shape[1] * scale_percent / 100)
ah = int(bounce.shape[0] * scale_percent / 100)
dim = (aw, ah)
bounce = cv2.resize(bounce,dim,interpolation=cv2.INTER_AREA)

path_back = "/home/jonne/back_up/PROJEKTIT/Screensaver/back.png"
frame = cv2.imread(path_back,1)

alpha = 0

speed_x = 3
speed_y = 3

# The size of moving image
w_o = bounce.shape[1]
h_o = bounce.shape[0]

# Starting location
x = 150
y = 150

# Boundaries
(h_b,w_b,_) = frame.shape

# The output video
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('EME.mp4', fourcc, 60.0, (1920,1080))

while(True):

    (x,y)  = new_position(x,y,speed_x,speed_y)

    if(x >= w_b-w_o-2 or x <= 2):
        speed_x = speed_x*(-1)
    elif(y >= h_b-h_o-2 or y <= 2):
        speed_y = speed_y*(-1)

    frame = cv2.imread(path_back,1)
    added = cv2.addWeighted(frame[y:y+h_o,x:x+w_o,:],alpha,bounce[0:h_o,0:w_o,:],1-alpha,0)
    frame[y:y+h_o,x:x+w_o] = added

    cv2.imshow('Screensaver', frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
