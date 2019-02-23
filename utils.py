import cv2 as cv
import numpy as np
import math

from point import Point

def create_blank(image):
    width, height = image.shape
    blank = np.ones((width, height), np.uint8)
    for i in range(0, width):
        for j in range(0, height):
            blank[i][j] = blank[i][j]*255
    return(blank)

def distance(A, B):
    distance = math.sqrt((A.x-B.x)**2 + (A.y-B.y)**2)
    return(distance)


    
    
    
