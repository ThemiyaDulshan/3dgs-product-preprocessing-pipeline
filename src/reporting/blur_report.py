import json
from pathlib import Path


def generate_blur_report(manifest, threshold, output_path):

    report = {

        "total_images": len(manifest),

        "kept_images": int((manifest["blur_status"] == "kept").sum()),

        "rejected_images": int((manifest["blur_status"] == "rejected").sum()),

        "average_blur_score": round(manifest["blur_score"].mean(), 2),

        "minimum_blur_score": round(manifest["blur_score"].min(), 2),

        "maximum_blur_score": round(manifest["blur_score"].max(), 2),

        "threshold": threshold

    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file:

        json.dump(report, file, indent=4)