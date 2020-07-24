
#
#   There are two option for return type "image" and "print".
#   If you select "image" it will show result as image .
#   Otherwise result will be shown as coordinates.
#   Use http://www.mazegenerator.net/ for maze generating purposes
#   Because at this stage this script recognizes maze generated from link above.    
#   

from Solver.engine import startMazeSolver
from Solver.ASTAR import *
import numpy
import cv2
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler()
    ]
)



if(len(sys.argv)!=3):
    logging.error("Error occured given arguments more or less than wanted")
    sys.exit(-1)
else:
    args=list(sys.argv)  # first arg is image_path second is return type
    
    ret=startMazeSolver(args[1].lower(),args[2].lower())
    
    if(isinstance(ret,numpy.ndarray)):
        cv2.imshow("image",ret)
        cv2.waitKey(10000)
        cv2.imwrite("./maze_solved1.png",ret)
    else:
        print(ret)

