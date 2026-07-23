from pathlib import Path

import yaml

from src.cleaning.dataset_selector import DatasetSelector

from src.utils.logger import setup_logger

from src.utils.manifest import (

    load_manifest,

    save_manifest,

    ensure_column

)

logger=setup_logger()

with open("configs/config.yaml") as file:

    config=yaml.safe_load(file)

manifest_path=Path(config["paths"]["manifest"])

manifest=load_manifest(manifest_path)

manifest=ensure_column(

    manifest,

    "selected_for_colmap",

    False

)

selector=DatasetSelector(

    config["selection"]["reject_blurry"],

    config["selection"]["reject_duplicates"],

    config["selection"]["reject_overexposed"],

    config["selection"]["reject_underexposed"]

)

for index,row in manifest.iterrows():

    manifest.loc[index,"selected_for_colmap"]=selector.should_keep(row)

save_manifest(

    manifest,

    manifest_path

)

import json

selected = int(manifest["selected_for_colmap"].sum())

report = {
    "total_images": len(manifest),
    "selected_images": selected,
    "removed_images": len(manifest) - selected
}

with open("reports/shoe_selection_report.json", "w") as f:
    json.dump(report, f, indent=4)

logger.info("Dataset selection completed.")