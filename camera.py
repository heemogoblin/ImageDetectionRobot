import picamera

FILE_NAME = 'snap.jpg'

def take_picture():
    camera = picamera.PiCamera()
    camera.capture(FILE_NAME)
