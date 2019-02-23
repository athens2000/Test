import cv2 as cv
import numpy as np

from lineOperations import intersection
from angle import Angle

def make_angle(lineM, lineN):
    meet = intersection(lineM, lineN)
    A = Angle(lineM.endPoint1, meet, lineN.endPoint1)
    B = Angle(lineM.endPoint1, meet, lineN.endPoint2)
    C = Angle(lineM.endPoint2, meet, lineN.endPoint1)
    D = Angle(lineM.endPoint2, meet, lineN.endPoint2)
    return(A, B, C, D)

def make_angles(allLines):
    allAngles = []
    for i in range(len(allLines)-1):
        for j in range(1, len(allLines)):
            if(i != j):
                angle = []
                A, B, C, D = make_angle(allLines[i], allLines[j])
                angle = [A, B, C, D]
                allAngles.append(angle)
    return(allAngles)
                
