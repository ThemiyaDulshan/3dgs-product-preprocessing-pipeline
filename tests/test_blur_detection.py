import numpy as np

from src.cleaning.blur_detector import BlurDetector


def test_detector():

    detector = BlurDetector()

    image = np.zeros((100,100,3),dtype=np.uint8)

    score = detector.calculate_blur(image)

    assert score >= 0