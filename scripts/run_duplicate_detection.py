from pathlib import Path
import yaml

from src.cleaning.duplicate_detector import DuplicateDetector
from src.utils.manifest import (
    load_manifest,
    save_manifest,
    ensure_column
)
from src.utils.logger import setup_logger

logger = setup_logger()

with open("configs/config.yaml", "r") as file:
    config = yaml.safe_load(file)

manifest_path = Path(config["paths"]["manifest"])

manifest = load_manifest(manifest_path)

manifest = ensure_column(manifest, "duplicate_group", -1)
manifest = ensure_column(manifest, "keep_image", True)
manifest = ensure_column(manifest, "hash_distance", 0)

detector = DuplicateDetector(
    threshold=config["duplicates"]["threshold"]
)

logger.info("Starting duplicate detection...")

group = 0

previous_hash = None

for index, row in manifest.iterrows():

    current_hash = detector.calculate_hash(row["filepath"])

    if previous_hash is None:

        manifest.loc[index, "duplicate_group"] = group

        manifest.loc[index, "keep_image"] = True

    else:

        duplicate, distance = detector.are_duplicates(
            previous_hash,
            current_hash
        )

        manifest.loc[index, "hash_distance"] = distance

        if duplicate:

            manifest.loc[index, "duplicate_group"] = group

            manifest.loc[index, "keep_image"] = False

        else:

            group += 1

            manifest.loc[index, "duplicate_group"] = group

            manifest.loc[index, "keep_image"] = True

    previous_hash = current_hash

save_manifest(manifest, manifest_path)

logger.info("Duplicate detection complete.")