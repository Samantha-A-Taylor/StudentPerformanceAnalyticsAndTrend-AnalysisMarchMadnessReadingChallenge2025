"""
data_loader.py

Handles loading and basic validation of raw student performance data.
"""

from pathlib import Path
import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : str or Path
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    df = pd.read_csv(path)
    return df


def validate_columns(df: pd.DataFrame, required_columns: list[str]) -> None:
    """
    Ensure required columns exist in the dataframe.

    Raises ValueError if any columns are missing.
    """
    missing = [c for c in required_columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
