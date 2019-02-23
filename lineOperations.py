import cv2 as cv
import numpy as np

from line import Line, LineSegment
from point import Point
from angle import Angle

from utils import create_blank


def get_points(rho, theta):
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    return(x1, y1, x2, y2)

def get_line_data(allRho, allTheta):
    lineData = np.ndarray(shape=(0,4), dtype=int)
    for i in range(0, len(allRho)):
        rho = allRho[i]
        theta = allTheta[i]
        x1, y1, x2, y2 = get_points(rho, theta)
        lineData = np.append(lineData, [[x1,y1,x2,y2]], axis=0)
    return(lineData)

def make_lines(allRho, allTheta):
    lineData = get_line_data(allRho, allTheta)
    finalData = []
    for pts in lineData:
        A = Point([pts[0], pts[1]])
        B = Point([pts[2], pts[3]])
        line = Line(A, B)
        finalData.append(line)
    return(finalData)

def make_segment(allPoints):
    left_most = Point([10000, 10000])
    right_most = Point([0, 0])
    for point in allPoints:
        if(point.x <= left_most.x):
            left_most = point
            
    for point in allPoints:
        if(point.x >= right_most.x):
            right_most = point

    segment = LineSegment(left_most, right_most)
    return(segment)
        
        

def intersection(lineM, lineN):
    a1 = (lineM.endPoint2.y-lineM.endPoint1.y)
    b1 = (-(lineM.endPoint2.x-lineM.endPoint1.x))
    c1 = ((lineM.endPoint2.y*lineM.endPoint1.x)-(lineM.endPoint1.y*lineM.endPoint2.x))

    a2 = (lineN.endPoint2.y-lineN.endPoint1.y)
    b2 = (-(lineN.endPoint2.x-lineN.endPoint1.x))
    c2 = ((lineN.endPoint2.y*lineN.endPoint1.x)-(lineN.endPoint1.y*lineN.endPoint2.x))

    A = np.array([[a1,b1] , [a2,b2]])
    C = np.array([c1,c2])
    X = np.linalg.solve(A, C)

    if(np.allclose(np.dot(A,X), C)):
        for i in range(0, X.size):
            X[i] = int(round(X[i]))
        meet = Point(X)
        lineM.add_point(meet)
        lineN.add_point(meet)
        return(meet)

def differentiate_segments(allLines, image):
    allSegments = []
    for line in allLines:
        seg_flag = False
        blank = create_blank(image)
        allPoints = line.get_all_points(blank)
        for point in allPoints:
            if(image[point.x, point.y] == 255):
                allPoints.remove(point)
                seg_flag = True
                
        if(seg_flag):
            segment = make_segment(allPoints)
            allSegments.append(segment)
            allLines.remove(line)

        return(allLines, allSegments)
        
                
    
