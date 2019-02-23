import cv2 as cv
import numpy as np

from ingestion import ingestion
from lineOperations import make_lines, intersection, get_line_data, differentiate_segments
from angleOperations import make_angles, make_angle
from utils import create_blank

from point import Point
from angle import Angle
from line import Line

image = cv.imread('test1.png', 0)
blank = create_blank(image)

allRho, allTheta = ingestion(image)
allLines = make_lines(allRho, allTheta)
allLines, allSegments = differentiate_segments(allLines, image)
##allAngles = make_angles(allLines)

for line in allSegments:
    line.plot(blank)
cv.imshow('plot', blank)
cv.waitKey(0)


##for line in allLines:
##    line.display(blank)
##    line.endPoint1.plot(blank)
##    line.endPoint2.plot(blank)
##cv.imshow('plot', blank)
##cv.waitKey(0)
    



##blank = create_blank(image)
##
##a.display_image(blank)
##allLines[0].display_image(blank)
##allLines[1].display_image(blank)
##cv.imshow('image', blank)
##cv.waitKey(0)

##blank = create_blank(image)
##b = Angle(allLines[0], allLines[1], a)
##b.plot_angle(blank)
##cv.waitKey(0)

##blank = create_blank(image)
##A = Point([34, 78])
##B = Point([90, 120])
##A.plot(blank)
##B.plot(blank)
##plot_segment(A, B, blank)
##cv.waitKey(0)
