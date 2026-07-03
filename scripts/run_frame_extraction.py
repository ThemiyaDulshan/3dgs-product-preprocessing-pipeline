import json
from pathlib import Path

import yaml

from src.extraction.video_info import VideoInfo
from src.extraction.frame_extractor import FrameExtractor
from src.utils.logger import setup_logger

logger = setup_logger()

config = yaml.safe_load(open("configs/config.yaml"))

video_folder = Path(config["paths"]["input_video"])

output_folder = Path(config["paths"]["output_frames"])

report_folder = Path(config["paths"]["reports"])

report_folder.mkdir(exist_ok=True)

for video in video_folder.glob("*"):

    logger.info(f"Processing {video.name}")

    info = VideoInfo(video).get_info()

    output = output_folder / video.stem

    extractor = FrameExtractor(

        video,

        output,

        config["video"]["fps"],

        config["video"]["image_format"],

        config["video"]["jpeg_quality"]

    )

    saved = extractor.extract()

    info["frames_saved"] = saved

    report = report_folder / f"{video.stem}_frame_report.json"

    with open(report, "w") as file:

        json.dump(info, file, indent=4)

    logger.info(f"Saved {saved} frames.")