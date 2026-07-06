import cv2
import numpy as np


class ExposureAnalyzer:

    def __init__(self,
                 brightness_low=60,
                 brightness_high=190,
                 contrast_low=25):

        self.brightness_low = brightness_low
        self.brightness_high = brightness_high
        self.contrast_low = contrast_low

    def analyze(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        brightness = np.mean(gray)

        contrast = np.std(gray)

        if brightness < self.brightness_low:
            status = "underexposed"

        elif brightness > self.brightness_high:
            status = "overexposed"

        else:
            status = "normal"

        return {

            "brightness": round(float(brightness),2),

            "contrast": round(float(contrast),2),

            "exposure_status": status

        }