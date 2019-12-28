from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 90
camera.start_preview(alpha=100)
sleep(10)
camera.stop_preview()
