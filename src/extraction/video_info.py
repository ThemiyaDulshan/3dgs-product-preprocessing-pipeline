from pathlib import Path
import cv2


class VideoInfo:

    def __init__(self, video_path):

        self.video_path = Path(video_path)

        self.capture = cv2.VideoCapture(str(self.video_path))

    def get_info(self):

        fps = self.capture.get(cv2.CAP_PROP_FPS)

        total_frames = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))

        width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))

        height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        duration = total_frames / fps if fps else 0

        codec = int(self.capture.get(cv2.CAP_PROP_FOURCC))

        return {

            "filename": self.video_path.name,

            "width": width,

            "height": height,

            "fps": fps,

            "duration": duration,

            "total_frames": total_frames,

            "codec": codec

        }