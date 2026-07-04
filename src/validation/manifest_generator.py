from pathlib import Path
import pandas as pd


class ManifestGenerator:
    """
    Creates the initial dataset manifest.
    Future modules will update this same manifest.
    """

    COLUMNS = [
        # Basic information
        "image_id",
        "filename",
        "filepath",

        # Validation
        "valid",
        "width",
        "height",
        "format",
        "file_size_kb",

        # Blur Detection
        "blur_score",
        "is_blurry",

        # Duplicate Detection
        "duplicate_group",
        "keep_image",

        # Exposure Analysis
        "brightness",
        "contrast",
        "is_overexposed",
        "is_underexposed",

        # Segmentation
        "mask_path",
        "mask_generated",

        # Final Selection
        "selected",

        # Errors
        "error"
    ]

    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def save(self, output_file):

        df = pd.DataFrame(self.records)

        # Ensure all columns exist
        for column in self.COLUMNS:
            if column not in df.columns:
                df[column] = None

        # Arrange columns
        df = df[self.COLUMNS]

        Path(output_file).parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output_file, index=False)

        return df