from L1TrackingBPR_APGup import L1TrackingBPR_APGup
from numpy import matrix as MA
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import cv2
import matplotlib.cm as cm
import matplotlib
import numpy as np


def tellme(s):
    print(s)
    plt.title(s,fontsize=10)
    plt.draw()
	#Initialization for the first frame. 
	#Each column is a point indicating a corner of the target in the first image. 
	#The 1st row is the y coordinate and the 2nd row is for x.
	#Let [p1 p2 p3] be the three points, they are used to determine the affine parameters of the target, as following
	# p1(65,55)-----------p3(170,53)
	#         |                 |
	#         |     target      |
	#         | 		    |
	#   p2(64,140)--------------
	# % size of template    
t = 0;
#Movie = cv2.VideoCapture("Videos/RobotNewSetup.avi")
#f,img = Movie.read()
img= cv2.imread('/home/ankush/Desktop/CleanCode/PythonTracker/Videos/BenchMark/Dudek/img/0001.jpg')
#img = cv2.imread('/home/ankush/Desktop/CleanCode/PythonTracker/Videos/Robot/RobotNewSetup/imagelocalnew-{0:10d}.ppm'.format(t));
plt.imshow(img)
pts = [];
while len(pts) < 4:
	tellme('Select 4 corners with mouse anticlockwise starting with top left')
	pts = np.asarray( plt.ginput(4,timeout=-1) )
	if len(pts) < 4:
		tellme('Too few points, starting over')
		time.sleep(1) # Wait a second
plt.close()
class para():
	def __init__(self):
		self.lambd = MA([[0.2,0.001,10]])
		self.angle_threshold = 50
		self.Lip = 8 ;
		self.Maxit = 5 ; 
		self.nT = 30; # number of templates for the sparse representation
		self.rel_std_afnv =  MA([[0.005,0.003,0.005,0.003,1,1]]) ; # diviation of the sampling of particle filter
		self.n_sample = 600; # No of particles
		self.sz_T = MA([[12,15]]); # Reshape each image so that they have the same image space representation
		# self.init_pos = MA([[360,520,360], [80,100,150]]); # juice
		# self.init_pos = MA([[280,455,275],[320,330,440]]) # book in shelf
		# self.init_pos = MA([[415,465,415],[360,360,410]])  # drinking from cup
		# self.init_pos = MA([[315,358,315],[302,302,350]]);
		# self.init_pos = MA([[385,500,385],[462,462,600]]); # MARS Rover
		self.init_pos = MA([[int(pts[0,1]),int(pts[1,1]),int(pts[2,1])],[int(pts[0,0]),int(pts[1,0]),int(pts[2,0])]])
               # self.init_pos = MA([[121,172,121],[58,58,109]]);#SYLV
#		self.bDebug = 0; # debugging indicator
		#self.bShowSaveImag = 1 ; # indicator for result image show and save after tracking finished
def main():
	paraT = para()
	L1TrackingBPR_APGup(paraT)


if __name__ == '__main__':
	main()
