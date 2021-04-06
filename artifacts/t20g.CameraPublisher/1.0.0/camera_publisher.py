#!/user/bin/env python
import argparse
from picamera import PiCamera
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("camera_interval", type=int)
args = parser.parse_args()

camera_preview_sleep = 5
camera_interval_remainder = args.camera_interval - camera_preview_sleep

print("Starting CameraPublisher with an interval of {} seconds".format(args.camera_interval))


while True:
    print ("Starting camera")
    camera = PiCamera()
    camera.start_preview()
    sleep(camera_preview_sleep)

    print("Taking picture")
    # Write image to the ML Work Directory for classification/detection
    camera.capture('/home/pi/GreenHouse/images/picture.jpg')
    camera.stop_preview()
    camera.close()
    sleep(camera_interval_remainder)
