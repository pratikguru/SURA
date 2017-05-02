from SimpleCV import *
import sys

#from basic import*

class CameraCapture():
        
    _key = True
    _width = 640
    _height = 480
    def __init__(self,index,width = 640, height = 480):
        self.width = width
        self.height = height
        self.cam = Camera(index,prop_set={"width":self.width,"height":self.height})
            
        
    def getNewImage(self):
        img = self.cam.getImage()
        csv = img
        return csv
        
    def getNewImage2(self):
        img = self.cam.getImage()
        csv = img/2
        return csv



index1 = 0
index2 = 1 
        #Make two camera objects 
cam1 = CameraCapture(index1)
cam2 = CameraCapture(index2)
width = cam1.width+cam2.width
disp = Display((width,cam1.height),0,'SURA Video feed')


def play():
        while disp.isNotDone():
            img1 = cam1.getNewImage()
            img2 = cam2.getNewImage()
            img3 = img1.sideBySide(img2)
            #draw text
            img3.drawText("Camera 1",100,400,fontsize=40,color=Color.BLUE)
            img3.drawText("Camera 2",840,400,fontsize=40,color=Color.GREEN)
            img3.save(disp)
            #
            


def play2():
         while disp.isNotDone():
            img1 = cam1.getNewImage2()
            img2 = cam2.getNewImage2()
            img3 = img1.sideBySide(img2)
            #draw text
            img3.drawText("Camera 1",100,400,fontsize=40,color=Color.BLUE)
            img3.drawText("Camera 2",840,400,fontsize=40,color=Color.GREEN)
            img3.save(disp)
            #
            

play()


