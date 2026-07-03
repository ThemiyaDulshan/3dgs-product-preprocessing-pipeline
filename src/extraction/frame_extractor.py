from pathlib import Path
import cv2


class FrameExtractor:

    def __init__(

            self,

            video_path,

            output_directory,

            fps,

            image_format,

            jpeg_quality):

        self.video_path = Path(video_path)

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(parents=True, exist_ok=True)

        self.capture = cv2.VideoCapture(str(video_path))

        self.original_fps = self.capture.get(cv2.CAP_PROP_FPS)

        self.frame_interval = int(self.original_fps / fps)

        self.image_format = image_format

        self.jpeg_quality = jpeg_quality

    def extract(self):

        frame_count = 0

        saved = 0

        while True:

            success, frame = self.capture.read()

            if not success:

                break

            if frame_count % self.frame_interval == 0:

                filename = self.output_directory / f"frame_{saved:06d}.{self.image_format}"

                cv2.imwrite(

                    str(filename),

                    frame,

                    [cv2.IMWRITE_JPEG_QUALITY, self.jpeg_quality]

                )

                saved += 1

            frame_count += 1

        self.capture.release()

        return saved