import cv2 as cv
import numpy as np

class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.x = int(coordinates[0])
        self.y = int(coordinates[1])

    def check(self):
       flag = False
       return(flag)

    def plot(self, image):
        cv.circle(image, (self.x, self.y), 5, (0,0,255),2)
        cv.imshow('plot', image)
