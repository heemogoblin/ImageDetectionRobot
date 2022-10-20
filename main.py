
import os, io
from google.cloud import vision
import motors
import camera
import line
from time import sleep, strftime, localtime
import distance

def debug(msg):
        print("[" + strftime('%a, %d %b %Y %H:%M:%S GMT', localtime()) + "]:", msg)

class Robot:

    def __init__(self):
        self.motorControl = motors.Motors()
        self.amt_turn = 1.0
        self.amt_forward = 0.05
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/pi/ai-app/robot/Client-secrets.json'
        self.client = vision.ImageAnnotatorClient()
        self.lineSensor = line.LineSensor()
        self.distanceMeasurer = distance.DistanceMeasurer()

    def run(self):
        while True:
            if self.lineSensor.is_on_line():
                #camera.take_picture() # is buggy
                debug("Line present, taking picture")
                os.system("raspistill -o snap.jpg")

                with io.open(camera.FILE_NAME, 'rb') as image_file:
                    content = image_file.read()

                image = vision.Image(content=content)
                response = self.client.text_detection(image=image)
                print(response)
                texts = response.text_annotations
                if len(texts) > 0:
                    found = False
                    for text in texts: 
                        data = text.description

                        for d in data:
                            n = ord(d)
                            if n == 70:
                                debug("Moving forward")
                                #Move forward
                                self.forward()
                                found = True
                                break
                            elif n == 83:
                                debug("Stopping")
                                #stop
                                self.motorControl.stop_motors()
                                found = True
                                break
                            elif n == 82:
                                debug("Turning right")
                                #move right
                                self.right()
                                found =True
                                break
                            elif n == 76:
                                debug("Turning left")
                                #move left
                                self.left()
                                found = True
                                break
                        if found:
                            break

                    
                    if not found:
                        debug("No characters recognised")
                        self.forward()
                else:
                    debug("No characters recognised")
                    self.forward()
            else:
                debug("No line, continuing straight")
                self.forward()

    def left(self):
        while self.distanceMeasurer.distance_left() < 40 or self.distanceMeasurer.distance_front_left() < 40:
            self.forward()
            debug("Avoiding obstacle on the left")
        self.motorControl.left(self.amt_turn)

    def right(self):
        while self.distanceMeasurer.distance_right() < 40 or self.distanceMeasurer.distance_front_right() < 40:
            self.forward()
            debug("Avoiding obstacle on the right")
        self.motorControl.right(self.amt_turn)

    def forward(self):
        if self.distanceMeasurer.distance_forward() > 10:
            """
            newleft = self.distanceMeasurer.distance_left()
            newright = self.distanceMeasurer.distance_right()
            if newleft < self.last_left and newright > self.last_right:
                self.motorControl.right(0.1)
            elif newleft > self.last_left and newright < self.last_right:
                self.motorControl.left(0.1)
            """
            self.motorControl.forward(self.amt_forward)
            if self.distanceMeasurer.distance_front_left() < 5:
                self.motorControl.right(0.1)
            elif self.distanceMeasurer.distance_front_right() < 5:
                self.motorControl.left(0.1)
            sleep(0.1)
        else:
            self.motorControl.stop_motors()
            debug("Obstacle ahead")

    

if __name__ == "__main__":
    robot = Robot()
    while True:
        robot.run()
