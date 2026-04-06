from pathlib import Path

import pandas as pd

LAB_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV_PATH = LAB_ROOT / "data" / "customers.csv"

TARGET_COLUMN = "will_buy"
FEATURE_COLUMNS = ["age", "monthly_spend", "visits_last_month", "city"]
NUMERIC_COLUMNS = ["age", "monthly_spend", "visits_last_month"]
CATEGORICAL_COLUMNS = ["city"]


def load_csv(csv_path: Path = DEFAULT_CSV_PATH) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned = cleaned.drop_duplicates()

    for column in NUMERIC_COLUMNS:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    cleaned["city"] = cleaned["city"].astype("string").str.strip()
    cleaned["city"] = cleaned["city"].replace({"": pd.NA, "nan": pd.NA, "None": pd.NA})

    for column in NUMERIC_COLUMNS:
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())

    city_mode = cleaned["city"].mode().iloc[0]
    cleaned["city"] = cleaned["city"].fillna(city_mode)

    cleaned[TARGET_COLUMN] = pd.to_numeric(cleaned[TARGET_COLUMN], errors="coerce")
    cleaned = cleaned.dropna(subset=[TARGET_COLUMN])
    cleaned[TARGET_COLUMN] = cleaned[TARGET_COLUMN].astype(int)

    return cleaned
