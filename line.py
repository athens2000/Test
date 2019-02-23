import cv2 as cv
import numpy as np

from point import Point


class Line:
    def __init__(self, endPoint1, endPoint2):
        self.endPoint1 = endPoint1
        self.endPoint2 = endPoint2
        self.allPoints = []
        self.allData = []
    

    def check(self):
        flag = False
        if(self.endPoint1.x != self.endPoint2.x and self.endPoint1.y != self.endPoint2.y):
            flag = True
        return(flag)

    def add_point(self, Point):
        self.allPoints.append(Point)

    def get_all_points(self, blank):
        cv.line(blank,(self.endPoint1.x,self.endPoint1.y),(self.endPoint2.x,self.endPoint2.y),(0,0,255),1)
        width, height = blank.shape
        for i in range(width):
            for j in range(height):
                if(blank[i][j] == 0):
                    pt = Point([i, j])
                    self.allData.append(pt)
        return(self.allData)

    def plot(self, blank):
        data = self.get_all_points(blank)
        width, height = blank.shape
        for pts in data:
            blank[pts.x][pts.y] = 0
        cv.imshow('plot', blank)

    def display(self, image):
        cv.line(image,(self.endPoint1.x,self.endPoint1.y),(self.endPoint2.x,self.endPoint2.y),(0,0,255),2)
        cv.imshow('plot', image)

class LineSegment:
    def __init__(self, endPoint1, endPoint2):
        self.endPoint1 = endPoint1
        self.endPoint2 = endPoint2
        self.allPoints = []
        self.allData = []

    def check(self):
        flag = False
        if(self.endPoint1.x != self.endPoint2.x and self.endPoint1.y != self.endPoint2.y):
            flag = True
        return(flag)

    def add_point(self, Point):
        self.allPoints.append(Point)

    def plot(self, blank):
        cv.line(blank, (self.endPoint1.x,self.endPoint1.y), (self.endPoint2.x,self.endPoint2.y), (0,0,255), 1)
        lineData = []
        width, height = blank.shape
        for i in range(0, width):
            for j in range(0, height):
                if(blank[i][j] == 0):
                    pt = Point([i,j])
                    lineData.append(pt)
                    blank[i][j] = 255
        for pt in lineData:
            if(np.sign([self.endPoint1.x-pt.x]) == np.sign([self.endPoint2.x-pt.x]) and np.sign([self.endPoint1.y-pt.y]) == np.sign([self.endPoint2.y-pt.y])):
                lineData.remove(pt)

        for pt in lineData:
            blank[pt.x][pt.y] = 0
        cv.imshow('plot', blank)

    def get_all_points(self, blank):
        self.plot(blank)
        width, height = blank.shape
        for i in range(width):
            for j in range(height):
                if(blank[i][j] == 0):
                    pt = Point([i, j])
                    self.allData.append(pt)
        return(self.allData)
        
        
        
        
        
        
    
        
