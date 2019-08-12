import cv2
import numpy as np
from PIL import ImageGrab
import time
import ctypes

# bbox = (450, 230, 500, 265)
# bbox = (Left, Top, Right, Bottom)
bbox = (865, 240, 950, 275)
shape = (bbox[3]-bbox[1], bbox[2]-bbox[0], 3)
bg = 255
ref_frame = np.full(shape, bg)

while True:
    img = ImageGrab.grab(bbox)
    frame = np.array(img)
    # frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame) 
    
    if bg != frame[0][0][0]:
        bg = frame[0][0][0]
        ref_frame = np.full(shape, bg)

    frame_diff = np.subtract(ref_frame, frame).sum()

    if frame_diff != 0:
        ctypes.windll.user32.keybd_event(0x20, 0, 0, 0)  # Space is down
        print(frame_diff)
    prev_frame = frame
 
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
