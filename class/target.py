import time
import colors
import logging
from datetime import datetime

""" This module detects objects using the ultrasonic and sends feedback to the main(radar) module"""
logging.basicConfig(filename='target.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')
class Target:
    angle = -1
    distance = -1
    time = -1.0
    color = ()
    # initalization
    def __init__(self, angle, distance):
        self.angle = angle
        self.distance = distance
        self.time = datetime.fromtimestamp(time.time())
        self.color = colors.red
        logging.info('Print Target info.: {} - {} - {} - {}'.format(self.angle,self.distance,self.color, self.time))
    def get_target(self): 
        return self.angle,self.distance,self.time,self.color
        #You can use the return statement to make your functions send Python objects back 
        # to the caller code. These objects are known as the function’s return value. 
        # You can use them to perform further computation in your programs.
Target(10,50)
