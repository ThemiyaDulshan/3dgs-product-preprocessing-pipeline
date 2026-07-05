from pathlib import Path

import cv2
import yaml

from src.cleaning.blur_detector import BlurDetector
from src.reporting.blur_report import generate_blur_report
from src.reporting.blur_histogram import save_histogram
from src.utils.logger import setup_logger
from src.utils.manifest import (
    load_manifest,
    save_manifest,
    ensure_column
)

logger = setup_logger()

# ------------------------
# Load configuration
# ------------------------

with open("configs/config.yaml", "r") as file:
    config = yaml.safe_load(file)

manifest_path = Path("data/manifests/shoe_manifest.csv")
dataset_name = manifest_path.stem.replace("_manifest", "")

manifest = load_manifest(manifest_path)

# ------------------------
# Ensure required columns exist
# ------------------------

manifest = ensure_column(manifest, "blur_score", 0.0)
manifest = ensure_column(manifest, "blur_status", "")

manifest["blur_score"] = manifest["blur_score"].astype(float)
manifest["blur_status"] = manifest["blur_status"].astype(str)

detector = BlurDetector(
    threshold=config["blur"]["threshold"]
)

logger.info("Starting blur detection...")

# ------------------------
# Process images
# ------------------------

for index, row in manifest.iterrows():

    image = cv2.imread(row["filepath"])

    if image is None:
        logger.warning(f"Could not read image: {row['filepath']}")
        continue

    score = detector.calculate_blur(image)

    manifest.loc[index, "blur_score"] = round(score, 2)

    if detector.is_blurry(score):
        manifest.loc[index, "blur_status"] = "rejected"
    else:
        manifest.loc[index, "blur_status"] = "kept"

# ------------------------
# Save manifest
# ------------------------

save_manifest(manifest, manifest_path)

logger.info("Blur detection complete.")

# ------------------------
# Reports
# ------------------------

generate_blur_report(
    manifest,
    config["blur"]["threshold"],
    f"reports/{dataset_name}_blur_report.json"
)

save_histogram(
    manifest,
    config["blur"]["threshold"],
    f"reports/{dataset_name}_blur_histogram.png"
)

logger.info("Reports generated successfully.")