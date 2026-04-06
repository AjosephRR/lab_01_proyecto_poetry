from pathlib import Path

from app.inference import predict_one
from app.training import train_and_save_model


def test_predict_one_returns_valid_output(tmp_path: Path) -> None:
    model_path = tmp_path / "model.joblib"
    train_and_save_model(model_path=model_path)

    payload = {
        "age": 37,
        "monthly_spend": 6800,
        "visits_last_month": 6,
        "city": "Guadalajara",
    }

    result = predict_one(payload, model_path=model_path)

    assert result["prediction"] in (0, 1)
    assert 0.0 <= result["probability_positive"] <= 1.0
