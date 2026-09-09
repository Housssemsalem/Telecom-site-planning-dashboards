"""Sanitized example of an ETL monitoring / data-quality check.

This file intentionally uses synthetic data and generic field names.
It is a portfolio example, not the original internship code.
"""

from datetime import datetime
import pandas as pd


REQUIRED_COLUMNS = ["site_id", "status", "operator", "technology"]


def validate_batch(df: pd.DataFrame) -> dict:
    """Run basic, reusable quality checks on an incoming batch."""
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]

    if missing_columns:
        return {
            "run_time": datetime.now().isoformat(timespec="seconds"),
            "status": "FAILED",
            "missing_columns": missing_columns,
            "row_count": len(df),
        }

    return {
        "run_time": datetime.now().isoformat(timespec="seconds"),
        "status": "OK",
        "missing_columns": [],
        "row_count": len(df),
        "null_site_ids": int(df["site_id"].isna().sum()),
        "duplicate_site_ids": int(df["site_id"].duplicated().sum()),
    }


def compare_batches(previous: pd.DataFrame, current: pd.DataFrame) -> dict:
    """Compare two sanitized batches and summarize changes."""
    previous_ids = set(previous["site_id"].dropna())
    current_ids = set(current["site_id"].dropna())

    added = current_ids - previous_ids
    removed = previous_ids - current_ids

    return {
        "previous_rows": len(previous),
        "current_rows": len(current),
        "added_sites": len(added),
        "removed_sites": len(removed),
    }


if __name__ == "__main__":
    previous_batch = pd.DataFrame(
        [
            {"site_id": "SITE_001", "status": "ACTIVE", "operator": "OP_A", "technology": "4G"},
            {"site_id": "SITE_002", "status": "ACTIVE", "operator": "OP_A", "technology": "5G"},
        ]
    )

    current_batch = pd.DataFrame(
        [
            {"site_id": "SITE_001", "status": "ACTIVE", "operator": "OP_A", "technology": "4G"},
            {"site_id": "SITE_002", "status": "INACTIVE", "operator": "OP_A", "technology": "5G"},
            {"site_id": "SITE_003", "status": "ACTIVE", "operator": "OP_B", "technology": "5G"},
        ]
    )

    print("Quality check:", validate_batch(current_batch))
    print("Batch comparison:", compare_batches(previous_batch, current_batch))
