import matplotlib.pyplot as plt
from pathlib import Path


def save_histogram(manifest, threshold, output_path):

    plt.figure(figsize=(8,5))

    plt.hist(
        manifest["blur_score"],
        bins=30
    )

    plt.axvline(
        threshold,
        linestyle="--",
        linewidth=2
    )

    plt.title("Blur Score Distribution")

    plt.xlabel("Blur Score")

    plt.ylabel("Number of Images")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(output_path)

    plt.close()