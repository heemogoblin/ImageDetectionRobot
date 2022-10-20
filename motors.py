#Motor a = pins 9 and 10
#9 = backwards, 10 = forwards
#motor b = 7 and 8
#8 is forwards, 7 is backwards


import RPi.GPIO  as GPIO
import time


class Motors:
    #Properties - motor pins
    motorbbackward = 7
    motorbforward = 8
    motorabackward = 9
    motoraforward = 10
    
    #Constructor method
    
    def __init__(self):
        #Sets mode & warnings
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.motorabackward, GPIO.OUT)
        GPIO.setup(self.motoraforward, GPIO.OUT)
        GPIO.setup(self.motorbbackward, GPIO.OUT)
        GPIO.setup(self.motorbforward, GPIO.OUT)
        #print("__init__ executed")
    
    #Destructor method
    def __del__(self):
        self.stop_motors()
        GPIO.cleanup()
        #print("__del__ executed")
    
    def stop_motors(self):
        GPIO.output(self.motorabackward,0)
        GPIO.output(self.motoraforward,0)
        GPIO.output(self.motorbbackward,0)
        GPIO.output(self.motorbforward,0)
        #print("stopping")
    def forward(self, amt):
        GPIO.output(self.motorabackward,0)
        GPIO.output(self.motoraforward,1)
        GPIO.output(self.motorbbackward,0)
        GPIO.output(self.motorbforward,1)
        #print("forward")
        time.sleep(amt)
        self.stop_motors()
    def backward(self):
        GPIO.output(self.motorabackward,1)
        GPIO.output(self.motoraforward,0)
        GPIO.output(self.motorbbackward,1)
        GPIO.output(self.motorbforward,0)
        #print("back")
        time.sleep(0.1)
        self.stop_motors()
    def left(self, amt):
        GPIO.output(self.motorabackward,1)
        GPIO.output(self.motoraforward,0)
        GPIO.output(self.motorbbackward,0)
        GPIO.output(self.motorbforward,1)
        #print("left")
        time.sleep(amt)
        self.stop_motors()
    def right(self, amt):
        GPIO.output(self.motorabackward,0)
        GPIO.output(self.motoraforward,1)
        GPIO.output(self.motorbbackward,1)
        GPIO.output(self.motorbforward,0)
        #print("right")
        time.sleep(amt)
        self.stop_motors()

if __name__ == "__main__":
    motor = Motors()
    motor.right(1.2)
