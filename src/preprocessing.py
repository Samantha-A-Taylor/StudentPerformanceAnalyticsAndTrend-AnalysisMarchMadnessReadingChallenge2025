"""
preprocessing.py

Data cleaning and feature engineering.
"""

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning:
    - Drop duplicates
    - Handle missing values

    Returns cleaned DataFrame.
    """
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    return df


def add_time_features(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Add derived time-based features from a date column.
    """
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

    df["year"] = df[date_column].dt.year
    df["month"] = df[date_column].dt.month
    df["week"] = df[date_column].dt.isocalendar().week

    return df
