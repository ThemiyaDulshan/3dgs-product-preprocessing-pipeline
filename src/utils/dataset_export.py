from pathlib import Path
import shutil


class DatasetExporter:

    def __init__(self, output_root):

        self.output_root = Path(output_root)

    def export(self, manifest, dataset_name):

        output = self.output_root / dataset_name

        output.mkdir(parents=True, exist_ok=True)

        copied = 0

        for _, row in manifest.iterrows():

            if not row["selected_for_colmap"]:
                continue

            source = Path(row["filepath"])

            destination = output / source.name

            shutil.copy2(source, destination)

            copied += 1

        return copied