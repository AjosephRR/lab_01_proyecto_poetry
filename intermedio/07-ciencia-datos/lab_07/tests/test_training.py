from pathlib import Path

from app.training import train_and_save_model


def test_train_and_save_model_creates_artifact(tmp_path: Path) -> None:
    model_path = tmp_path / "model.joblib"

    report = train_and_save_model(model_path=model_path)

    assert model_path.exists()
    assert report["rows_after_cleaning"] > 0
    assert report["train_rows"] > 0
    assert report["test_rows"] > 0
    assert 0.0 <= report["accuracy"] <= 1.0
