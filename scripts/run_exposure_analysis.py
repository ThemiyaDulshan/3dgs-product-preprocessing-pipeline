from pathlib import Path

import cv2
import yaml

from src.cleaning.exposure_analyzer import ExposureAnalyzer
from src.utils.manifest import (
    load_manifest,
    save_manifest,
    ensure_column
)
from src.utils.logger import setup_logger

logger = setup_logger()

with open("configs/config.yaml") as file:
    config = yaml.safe_load(file)

manifest_path = Path(config["paths"]["manifest"])

manifest = load_manifest(manifest_path)

manifest = ensure_column(manifest,"brightness",0.0)
manifest = ensure_column(manifest,"contrast",0.0)
manifest = ensure_column(manifest,"exposure_status","")

analyzer = ExposureAnalyzer(

    config["exposure"]["brightness_low"],

    config["exposure"]["brightness_high"],

    config["exposure"]["contrast_low"]

)

logger.info("Starting exposure analysis...")

for index,row in manifest.iterrows():

    image = cv2.imread(row["filepath"])

    if image is None:
        continue

    result = analyzer.analyze(image)

    manifest.loc[index,"brightness"] = result["brightness"]

    manifest.loc[index,"contrast"] = result["contrast"]

    manifest.loc[index,"exposure_status"] = result["exposure_status"]

save_manifest(manifest,manifest_path)

logger.info("Exposure analysis complete.")

from src.reporting.exposure_report import generate_exposure_report
from src.reporting.exposure_histogram import save_exposure_histogram

dataset_name = manifest_path.stem.replace("_manifest","")

generate_exposure_report(
    manifest,
    f"reports/{dataset_name}_exposure_report.json"
)

save_exposure_histogram(
    manifest,
    f"reports/{dataset_name}_brightness_histogram.png"
)