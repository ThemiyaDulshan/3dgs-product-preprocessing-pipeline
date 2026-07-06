from PIL import Image
import imagehash


class DuplicateDetector:

    def __init__(self, threshold=5):
        self.threshold = threshold

    def calculate_hash(self, image_path):

        image = Image.open(image_path)

        return imagehash.phash(image)

    def are_duplicates(self, hash1, hash2):

        distance = hash1 - hash2

        return distance <= self.threshold, distance