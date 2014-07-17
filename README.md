L1 Tracker
-------------

Packages
 -----------
 
1. Python
2. OpenCV
3.  C Compiler

Usage
----------
 
1. Make the c files `make`.
2. Open the main file, main.py , given the location of the first image and allow user to specify which region to track `img = `
2. Open the main file, set the path for the images, `self.path =  `
3. Set the path for the folder where the tracked images are to be stored `self.results =  `
4. You can set other parameters for the particle filter in this main file
5. If tracked images are to be saved uncomment `cv2.imwrite' in L1TrackingBPR_APGup.py
