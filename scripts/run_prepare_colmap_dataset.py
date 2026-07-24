from pathlib import Path

import json
import yaml

from src.utils.dataset_export import DatasetExporter
from src.utils.logger import setup_logger
from src.utils.manifest import load_manifest

logger = setup_logger()

with open("configs/config.yaml") as file:
    config = yaml.safe_load(file)

manifest_path = Path(config["paths"]["manifest"])

manifest = load_manifest(manifest_path)

dataset_name = manifest_path.stem.replace("_manifest", "")

exporter = DatasetExporter(
    config["paths"]["selected_images"]
)

logger.info("Preparing dataset for COLMAP...")

count = exporter.export(
    manifest,
    dataset_name
)

report = {

    "dataset": dataset_name,

    "selected_images": count

}

Path("reports").mkdir(exist_ok=True)

with open(
    f"reports/{dataset_name}_export_report.json",
    "w"
) as file:

    json.dump(report, file, indent=4)

logger.info(f"Exported {count} images.")