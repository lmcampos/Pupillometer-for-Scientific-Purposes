#! /usr/bin/env python
# coding=utf-8

from tkinter import *
import threading
import time
from picamera import PiCamera
from tkinter import *

root = Tk() 
root.title("Pupilometro")
  
root.geometry("300x200") 

class Job(threading.Thread):
    def __init__ (self, name):
        super().__init__()
        self.shutdown_flag = threading.Event()
        self.name = name
        
    
    def run(self):
        
        if self.name == "video": 
            print("inicio la grabación") 
            camera = PiCamera()
            camera.resolution = (640,480)
            camera.framerate = 120 
            camera.start_preview()
            camera.start_recording('/home/pi/Desktop/video.h264')

        while not self.shutdown_flag.is_set():

            self.shutdown_flag.wait(0.1)
            if self.name == "censar":
                print("censando..")

        print('Thread #%s stopped' % self.name)
        
        if self.name == "video":
            camera.stop_recording()
            camera.stop_preview()
            print("detengo la grabación")
    
    def setThread(self):
        self.shutdown_flag.set()
j1 = Job("video")
j2 = Job("censar")

def grabar():
    j1.start()
    j2.start()
def salir():
    j1.setThread()
    j2.setThread()
            
#for i in range(10): 
        #print("Esperando",i,"segundo") 
        #time.sleep(1) 
#j1.setThread()
#j2.setThread()

Button(root,text="Iniciar Grabación",command = grabar).pack() 
Button(root,text="Detener Grabación",command = salir).pack()
root.mainloop()