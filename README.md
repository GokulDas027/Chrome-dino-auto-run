# Chrome-dino-auto-run
Autonomous Dino run using OpenCV and Numpy. The Running t-rex of 21st century.

.......................................![Auto Dino gif](https://drive.google.com/uc?export=view&id=19b1s_Y2N4Ez_gb3pfZaTL6Ha9TbnOnGI).......................................

![Autonomous Dino Highscore ss](https://drive.google.com/uc?export=view&id=1zPd9J8OaQM5FvLrO87DfLdGLAHlth8us)

### Working
It works by capturing a frame in front of the dino and comparing it with a reference frame of totally white or black pixels.
And if an obstacle is found, Spacebar is triggered and the Dino jumps. Also the Region of Interest(RoI) for frame capture is updated to
adapt with the increasing speed.

### Usage
The capturing Region of Interest must be tuned as per your display. By default it is tuned for 19" and chrome in half screen at right (as in figure)

### Improvements
The RoI updation could be tuned, to go beyond the High Score. It won't be hard to go till 10,000.
