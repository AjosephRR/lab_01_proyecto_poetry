from pathlib import Path
from typing import Any

import joblib
import pandas as pd

from app.training import DEFAULT_MODEL_PATH

LAB_ROOT = Path(__file__).resolve().parents[1]


def load_artifact(model_path: Path = DEFAULT_MODEL_PATH) -> dict[str, Any]:
    artifact = joblib.load(model_path)
    return artifact


def predict_one(
    payload: dict[str, Any],
    model_path: Path = DEFAULT_MODEL_PATH,
) -> dict[str, float | int]:
    artifact = load_artifact(model_path)

    model = artifact["model"]
    feature_columns = artifact["feature_columns"]

    input_df = pd.DataFrame([payload], columns=feature_columns)

    prediction = int(model.predict(input_df)[0])

    probability_positive = float(model.predict_proba(input_df)[0][1])

    return {
        "prediction": prediction,
        "probability_positive": round(probability_positive, 4),
    }


def main() -> None:
    sample_payload = {
        "age": 40,
        "monthly_spend": 7600,
        "visits_last_month": 7,
        "city": "Monterrey",
    }

    result = predict_one(sample_payload)

    print("Inferencia completada")
    print(f"Entrada: {sample_payload}")
    print(f"Predicción: {result['prediction']}")
    print(f"Probabilidad positiva: {result['probability_positive']}")


if __name__ == "__main__":
    main()
