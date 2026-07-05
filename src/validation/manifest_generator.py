from pathlib import Path
import pandas as pd


class ManifestGenerator:
    """
    Creates the initial dataset manifest.
    Future modules will update this same manifest.
    """

    COLUMNS = [
    "image_id",
    "filename",
    "filepath",

    "valid",
    "width",
    "height",
    "format",
    "file_size_kb",

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