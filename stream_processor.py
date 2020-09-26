from picamera import PiCamera
#import cv2
import io
import time


class StreamProcessor:

    def __init__(self, operation: str):
        self.IMG_H = 720
        self.IMG_W = 1280
        self.sample_size = 2
        self.export_image_name = f'{operation}_image.jpg'

    # Get frame and drop to image.jpeg
    def process_stream(self):
        cam = PiCamera()
        cam.resolution = (self.IMG_W, self.IMG_H)
        cam.framerate = 25
        for sample in range(self.sample_size):
            cam.start_preview()
            time.sleep(5)
            frame = cam.capture(self.export_image_name)
        cam.stop_preview()
        cam.close()
        return frame