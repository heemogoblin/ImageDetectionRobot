import os, io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Client-secrets.json'
client = vision.ImageAnnotatorClient()

FILE_NAMEs = input("Enter file name")
FILE_NAME = r'{}'.format(FILE_NAMEs)

with io.open(FILE_NAME, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.text_detection(image=image)
texts = response.text_annotations

data = texts[0].description

for d in data:
    n = ord(d)
    print(ord(d))
    if n == 70:
        print("Moving forward")
        #Move forward
    elif n == 83:
        print("Stopping")
        #stop
    elif n == 1042:
        print("Backwards")
        #move backwards
    elif n == 82:
        print("Turning right")
        #move right
    elif n == 76:
        print("Turning left")
        #move left
