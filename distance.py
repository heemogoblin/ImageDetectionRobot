
import RPi.GPIO as GPIO
import time

class DistanceMeasurer:

    FORWARD_TRIG = 24
    FORWARD_ECHO = 23
    LEFT_TRIG = 22
    LEFT_ECHO = 27
    RIGHT_TRIG = 5
    RIGHT_ECHO = 6
    FRONT_RIGHT_TRIG = 21
    FRONT_RIGHT_ECHO = 20
    FRONT_LEFT_TRIG = 26
    FRONT_LEFT_ECHO = 19

    def __init__(self):


        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.FORWARD_TRIG, GPIO.OUT)
        GPIO.setup(self.FORWARD_ECHO, GPIO.IN)
        GPIO.setup(self.LEFT_TRIG, GPIO.OUT)
        GPIO.setup(self.LEFT_ECHO, GPIO.IN)
        GPIO.setup(self.RIGHT_TRIG, GPIO.OUT)
        GPIO.setup(self.RIGHT_ECHO, GPIO.IN)
        GPIO.setup(self.FRONT_LEFT_TRIG, GPIO.OUT)
        GPIO.setup(self.FRONT_LEFT_ECHO, GPIO.IN)
        GPIO.setup(self.FRONT_RIGHT_TRIG, GPIO.OUT)
        GPIO.setup(self.FRONT_RIGHT_ECHO, GPIO.IN)

    def read_distance(self, TRIG, ECHO):
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        StartTime = time.time()
        StopTime = time.time()

        while GPIO.input(ECHO) == 0:
            StartTime = time.time()
        
        while GPIO.input(ECHO) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2

        return distance

    def distance_left(self):
        return self.read_distance(self.LEFT_TRIG, self.LEFT_ECHO)

    def distance_right(self):
        return self.read_distance(self.RIGHT_TRIG, self.RIGHT_ECHO)

    def distance_forward(self):
        return self.read_distance(self.FORWARD_TRIG, self.FORWARD_ECHO)

    def distance_front_left(self):
        return self.read_distance(self.FRONT_LEFT_TRIG, self.FRONT_LEFT_ECHO)

    def distance_front_right(self):
        return self.read_distance(self.FRONT_RIGHT_TRIG, self.FRONT_RIGHT_ECHO)
    
    def __del__(self):
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        d = DistanceMeasurer()
        while True:
            print("Distance forward:", d.distance_forward())
            print("Distance front left:", d.distance_front_left())
            print("Distance front right:", d.distance_front_right())
            print("Distance right:", d.distance_right())
            print("Distance left:", d.distance_left())
            print("")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopped")
