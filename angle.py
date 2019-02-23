import cv2 as cv
import numpy as np

from point import Point
from line import LineSegment


class Angle:
    def __init__(self, endPoint1, vertex, endPoint2):
        self.endPoint1 = endPoint1
        self.endPoint2 = endPoint2
        self.vertex = vertex
        self.allData = []

    def check(self):
        flag = False
        return(flag)

    def get_all_points(self, blank):
        ray1 = LineSegment(self.endPoint2, self.vertex)
        ray2 = LineSegment(self.endPoint1, self.vertex)
        ray1.plot(blank)
        ray2.plot(blank)
        
        width, height = blank.shape

        for i in range(width):
            for j in range(height):
                if(blank[i][j] == 0):
                    pt = Point([i, j])
                    self.allData.append(pt)
        return(self.allData)

    def plot(self, blank):
        for pts in self.allData:
            blank[pts.x][pts.y] = 0
        ray1 = LineSegment(self.endPoint2, self.vertex)
        ray2 = LineSegment(self.endPoint1, self.vertex)
        ray1.plot(blank)
        ray2.plot(blank)
        self.endPoint1.plot(blank)
        self.endPoint2.plot(blank)
        self.vertex.plot(blank)
        cv.imshow('plot', blank)


