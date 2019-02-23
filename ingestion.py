import numpy as np
import cv2 as cv

from lineOperations import get_points


def clear_double_lines(allLines):
    allRho = np.array([])
    allTheta = np.array([])
    counter = np.array([])
    rhoThresh = 25
    thetaThresh = 0.1

    for line in allLines:
        rho, theta = line[0]
        flag = True

        if(len(allRho) == len(allTheta)):
            lenght = len(allRho)
            for i in range (0, lenght):
                if(abs(rho-allRho[i]) < rhoThresh and abs(theta-allTheta[i]) < thetaThresh):
                    counter[i] = counter[i] + 1
                    allRho[i] = (allRho[i]*(counter[i]-1) + rho)/counter[i]
                    allTheta[i] = (allTheta[i]*(counter[i]-1) + theta)/counter[i]
                    flag = False
                    break
                
        if(flag):
            allRho = np.append(allRho, rho)
            allTheta = np.append(allTheta, theta)
            counter = np.append(counter, 1)
##    print(len(allRho))
##    print(counter)
    return(allRho, allTheta)


def ingestion(image):
    edges = cv.Canny(image,55,150,apertureSize = 3)
    lines = cv.HoughLines(edges,1,np.pi/180,140)
    allRho, allTheta = clear_double_lines(lines)
    return(allRho, allTheta)
    
