import cv2
import numpy as np
from PIL import ImageGrab # windows and mac
# import pyscreenshot as ImageGrab # linux
import ctypes
# import os # for linux key press
# bbox = (450, 230, 500, 265) fix
# bbox = (Left, Top, Right, Bottom)
bbox = (865, 240, 960, 275)
shape = (bbox[3]-bbox[1], bbox[2]-bbox[0], 3)
bg = 255
ref_frame = np.full(shape, bg)
i = 1

while True:
    # capturing the frame.
    img = ImageGrab.grab(bbox)
    frame = np.array(img)
    cv2.imshow("frame", frame)

    # updating the reference frame with the background change.
    # toggling between white frame and black frame.
    if bg != frame[0][0][0]:
        bg = frame[0][0][0]
        ref_frame = np.full(shape, bg)
        i += 1

    # comparing the captured frame and reference frame.
    frame_diff = np.subtract(ref_frame, frame).sum()

    # if frames aren't the same, obstacle detected and jump.
    if frame_diff != 0:
        ctypes.windll.user32.keybd_event(0x20, 0, 0, 0)  # Space is down
        # os.system('xdotool key space') # for linux
    # updating the frame capture region to adapt with the increasing speed.
    if i % 4 == 0:
        bbox = (bbox[0]+1, bbox[1], bbox[2]+1, bbox[3])
        shape = (bbox[3]-bbox[1], bbox[2]-bbox[0], 3)
        ref_frame = np.full(shape, bg)
        print(f"update {i}")
        i += 1

    # listen for ESC key to exit.
    if cv2.waitKey(1) == 27: # when ESC is pressed
        break

cv2.destroyAllWindows()
