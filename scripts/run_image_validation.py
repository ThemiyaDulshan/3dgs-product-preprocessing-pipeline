from pathlib import Path
import yaml

from src.validation.image_validator import ImageValidator
from src.validation.manifest_generator import ManifestGenerator
from src.utils.logger import setup_logger

logger = setup_logger()

config = yaml.safe_load(open("configs/config.yaml"))

frame_root = Path(config["paths"]["output_frames"])

manifest_folder = Path(config["paths"]["manifests"])

manifest_folder.mkdir(parents=True, exist_ok=True)

for product_folder in frame_root.iterdir():

    if not product_folder.is_dir():

        continue

    logger.info(f"Validating {product_folder.name}")

    manifest = ManifestGenerator()

    for image_id, image in enumerate(sorted(product_folder.glob("*")), start=1):

        record = ImageValidator(image).validate()

        record["image_id"] = image_id

        manifest.add(record)

    output = manifest_folder / f"{product_folder.name}_manifest.csv"

    manifest.save(output)

    logger.info(f"Manifest saved: {output}")