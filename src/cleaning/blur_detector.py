import cv2


class BlurDetector:

    def __init__(self, threshold=100):
        self.threshold = threshold

    def calculate_blur(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        score = cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()

        return score

    def is_blurry(self, score):

        return score < self.threshold