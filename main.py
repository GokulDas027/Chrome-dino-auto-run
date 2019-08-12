import cv2
import numpy as np
from PIL import ImageGrab
import time
import ctypes

# bbox = (450, 230, 500, 265) incorrect
# bbox = (Left, Top, Right, Bottom)
bbox = (865, 240, 960, 275)
shape = (bbox[3]-bbox[1], bbox[2]-bbox[0], 3)
bg = 255
ref_frame = np.full(shape, bg)
i = 1

while True:
    img = ImageGrab.grab(bbox)
    frame = np.array(img)
    # frame = cv2.cvtColor(np_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame) 
    
    if bg != frame[0][0][0]:
        bg = frame[0][0][0]
        ref_frame = np.full(shape, bg)
        i += 10
        print(i)

    frame_diff = np.subtract(ref_frame, frame).sum()

    if frame_diff != 0:
        ctypes.windll.user32.keybd_event(0x20, 0, 0, 0)  # Space is down
        
    if i % 11 == 0:
        bbox = (bbox[0]+1, bbox[1], bbox[2]+1, bbox[3])
        shape = (bbox[3]-bbox[1], bbox[2]-bbox[0], 3)
        ref_frame = np.full(shape, bg)

    if cv2.waitKey(1) == 27: # when ESC is pressed
        break
cv2.destroyAllWindows()
