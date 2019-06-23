#!/usr/bin/env python
import os
import fcntl
import struct
from datetime import datetime, timedelta
from time import sleep, strftime
import logging
from logging.handlers import TimedRotatingFileHandler
import glob
import shutil
from ISStreamer.Streamer import Streamer
import math
import requests
import json
import random
import redis
import select
import signal
import requests
import os
from picamera import PiCamera
from time import sleep
import click

import anvil.server


class CoffeeScale:
    def __init__(self):
        
       
       
        self._currentWeight = 0


        
        self._environment = ''
       



    def getWeightInGrams(self, dev="/dev/usb/hiddev0"):
      

        grams = -1
        try:
            with open(dev, 'r+b') as f:
                # Read 4 unsigned integers from USB device
                fmt = "IIII"
                bytes_to_read = struct.calcsize(fmt)
                r = f.read(bytes_to_read)
                usb_binary_read = struct.unpack(fmt, r)
                if len(usb_binary_read) == 4: 
                    grams = usb_binary_read[3]
        except OSError as e:
            print("{0} - Failed to read from USB device".format(datetime.utcnow()))
        return grams



    def main(self):
        self._currentWeight = self.getWeightInGrams()
        camera=PiCamera()
        take_picture = True
        while True:
            
	  

            tmpWeight = self.getWeightInGrams()
                
        
            print tmpWeight
            
            if tmpWeight > 118 and tmpWeight < 135 and take_picture == True:
                print("A Potential Monster Appears")
                camera.start_preview()
                sleep(2)
                
                camera.capture('/home/pi/Desktop/monster.jpg')
                
                camera.stop_preview()
                sleep(5)
                tmpWeight = self.getWeightInGrams()
                if tmpWeight > 118 and tmpWeight < 135:
                        print("It'S NOt ImPOrtANt tO breW FResH CoFfEe!!1!")
                        URL="http://172.31.3.111:5000/api/test"
                        #URL="http://3.16.47.17:80/api/test"



                        
                       
                        data=open('/home/pi/Desktop/monster.jpg').read()
                        r=requests.post(URL,data=data)
                        #r=requests.post(URL,data={'picture':data, 'type':'bad'})
                        take_picture = False
                        
                #if tmpWeight > 135
                        #URL="http://172.31.3.111:5000/api/test"
                        #URL="http://3.16.47.17:80/api/test"
                        #data=open('/home/pi/Desktop/monster.jpg').read()
                        #r=requests.post(URL,data=data)


                        
                       
                        #data=open('/home/pi/Desktop/monster.jpg').read()
                        #r=requests.post(URL,data={'picture':data, 'type':'good'})
                        #take_picture = False
                        
            if tmpWeight>136 and take_picture == False:
                print("SWEET NECTAR!")
                take_picture = True       
                       
       

              



            
if __name__ == "__main__":
   
    scale = CoffeeScale()


    scale.main()


