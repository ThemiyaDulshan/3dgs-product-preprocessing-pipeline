import pandas as pd


def load_manifest(path):
    return pd.read_csv(path)


def save_manifest(df, path):
    df.to_csv(path, index=False)


def ensure_column(df, column_name, default_value=None):
    """
    Add a column only if it does not already exist.
    """
    if column_name not in df.columns:
        df[column_name] = default_value

    return df