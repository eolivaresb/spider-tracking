--What it is?
This is a simple script designed to track the movement of a spider in a maze.
It work on the specific lab conditions used in the test.avi video. However, it can be customize to work on different conditions.

--Dependences?
It's a python script tested in python 2.7.
You should have already installed Matplotlib, Numpy, OpenCV (cv2)
The script has been used in Linux, Mac and Windows.

-- How it work?
Execute the file tracking.py

In this file you should load the video that you wish to analyze.
The script will ask you information about the video in three instances:

1) A window with the maze is displayed in the screen.
Press the mouse left button on a extreme of the maze and release them in the other extreme. This value is used to convert pixels to centimeters.
If something went wrong press the mouse right button. the image should refresh.
If the line is fine, then press ESC.

2) Another window with the maze is displayed in the screen.
Press the mouse left button in the position of the spider.
If everything if fine, press ESC

3) The third window is displayed.
Mark the vertices of the maze. this step is important because the image analysis will be executed inside the polygon described by the points selected in this step.
Press SPACE BAR. the polygon will be displayed in a new window. If you are not happy with the selection, press the mouse right button on the first window, the points will be erased and you could select them again.
When the selection is correct, press ESC.

The tracking window will be displayed, press SPACE BAR to start the tracking.

Once the analysis is done there will be saved
- a file with successive positions described by the spider.
- a video showing the tracking.
- a plot showing some statistic related with the spider behavior in the maze.


-- Contact:
Any comment please write an email to erickolivaresb@gmail.com
Feel free to use, copy and modified.
