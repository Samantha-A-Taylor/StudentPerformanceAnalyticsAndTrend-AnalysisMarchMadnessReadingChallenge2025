"""
analysis.py

Core analytics and trend calculations.
"""

from pathlib import Path
import pandas as pd

from src.data_loader import load_csv, validate_columns
from src.preprocessing import clean_data, add_time_features


DATA_PATH = Path("data/raw/student_performance.csv")
OUTPUT_PATH = Path("data/processed")
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


REQUIRED_COLUMNS = [
    "student_id",
    "reading_minutes",
    "date"
]


def compute_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute summary statistics for reading performance.
    """
    summary = (
        df.groupby("student_id")["reading_minutes"]
        .agg(["count", "mean", "sum"])
        .reset_index()
        .rename(columns={
            "count": "sessions",
            "mean": "avg_minutes",
            "sum": "total_minutes"
        })
    )
    return summary


def run_analysis() -> None:
    """
    End-to-end analysis pipeline.
    """
    print("Loading data...")
    df = load_csv(DATA_PATH)

    validate_columns(df, REQUIRED_COLUMNS)

    print("Cleaning data...")
    df = clean_data(df)

    print("Adding time features...")
    df = add_time_features(df, "date")

    print("Computing summary statistics...")
    summary = compute_summary_statistics(df)

    output_file = OUTPUT_PATH / "student_summary.csv"
    summary.to_csv(output_file, index=False)

    print(f"Analysis complete. Results saved to {output_file}")


if __name__ == "__main__":
    run_analysis()
