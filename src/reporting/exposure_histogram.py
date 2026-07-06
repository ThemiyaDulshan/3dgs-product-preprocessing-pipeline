import matplotlib.pyplot as plt


def save_exposure_histogram(manifest,output_file):

    plt.figure(figsize=(8,5))

    plt.hist(manifest["brightness"],bins=30)

    plt.title("Brightness Distribution")

    plt.xlabel("Brightness")

    plt.ylabel("Images")

    plt.savefig(output_file)

    plt.close()