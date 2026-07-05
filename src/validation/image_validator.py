from pathlib import Path
from PIL import Image
import os


class ImageValidator:

    def __init__(self, image_path):

        self.image_path = Path(image_path)

    def validate(self):

        result = {

    "image_id": None,

    "filename": self.image_path.name,

    "filepath": str(self.image_path),

    "valid": False,

    "width": None,

    "height": None,

    "format": None,

    "file_size_kb": None,

    "error": None

}

        try:

            with Image.open(self.image_path) as image:

                image.verify()

            with Image.open(self.image_path) as image:

                result["width"] = image.width

                result["height"] = image.height

                result["format"] = image.format

            result["file_size_kb"] = round(
                os.path.getsize(self.image_path) / 1024,
                2
            )

            result["valid"] = True

        except Exception as e:

            result["error"] = str(e)

        return result