import sys
import cv2

c = 0
def extractImages(pathIn, pathOut,c):
    count = 0

    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    while success:
        success,image = vidcap.read()
        if count%20==0:
            #image = imutils.rotate_bound(image, 90)
            cv2.imwrite( pathOut + "%06d.jpg" % c, image)
            c = c + 1
        count = count + 1
    return c



s = "C0015.mp4"
pathIn = "K:/Data/UAV2022/Nadia_Video/2022_Summer_Proximal_Remote_Sensing_for_ML/Proximal_Sensing/Peas/08122022_Minot_Peas_4KSony_Video/%s" %s
pathOut = "D:/Image/C0015_Raw_Image"




c=extractImages(pathIn, pathOut,c)