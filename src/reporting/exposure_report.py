import json
from pathlib import Path


def generate_exposure_report(manifest,output_file):

    report={

        "total_images":len(manifest),

        "average_brightness":
            round(manifest["brightness"].mean(),2),

        "average_contrast":
            round(manifest["contrast"].mean(),2),

        "underexposed":
            int((manifest["exposure_status"]=="underexposed").sum()),

        "normal":
            int((manifest["exposure_status"]=="normal").sum()),

        "overexposed":
            int((manifest["exposure_status"]=="overexposed").sum())

    }

    Path(output_file).parent.mkdir(parents=True,exist_ok=True)

    with open(output_file,"w") as f:

        json.dump(report,f,indent=4)