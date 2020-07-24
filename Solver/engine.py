
import cv2
import numpy as np
from Solver.ASTAR import *
import logging
import time

def startMazeSolver(image_path="./maze.png",return_type="image",solver="astar"):
    try:
        img=cv2.imread(image_path)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    except Exception:
        logging.error("Error occured check provided maze path or file")
        return -1

    eroded=cv2.erode(img,kernel=np.ones((14,14),dtype=np.float32)/9)
    w,h=eroded.shape
    _start=None
    _end=None
    path=None
    result=None

    # find starting point and ending point

    for x in range(h):
        if(eroded[0][x]==255):
            _start=(0,x)
            break
    for x in range(h):
        if(eroded[w-1][x]==255):
            _end=(w-1,x)
            break
    
    # for now just A* algorithm added 
    if(solver.lower()=="astar"):
        tstart=time.time()
        path=Astar(_start,_end).start(eroded)
        logging.info("A* algorithm finished in {} seconds".format(time.time()-tstart))
    else:
        return
    
    if(return_type.lower()=="image"):
        img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        for move in path:
            img[move[0]][move[1]]=[0,0,255]
        result=img
    elif(return_type.lower()=="cor"):
        result=path
    else:
        logging.warning("Return type is unidentified !")
        result=-1
    return result
