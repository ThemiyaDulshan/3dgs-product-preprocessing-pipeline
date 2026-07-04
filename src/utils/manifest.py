import pandas as pd


def load_manifest(path):
    return pd.read_csv(path)


def save_manifest(df, path):
    df.to_csv(path, index=False)