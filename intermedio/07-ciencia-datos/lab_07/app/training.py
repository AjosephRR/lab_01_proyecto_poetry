from pathlib import Path

import joblib
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from app.data import (
    CATEGORICAL_COLUMNS,
    DEFAULT_CSV_PATH,
    FEATURE_COLUMNS,
    NUMERIC_COLUMNS,
    TARGET_COLUMN,
    clean_data,
    load_csv,
)

LAB_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_PATH = LAB_ROOT / "artifacts" / "customer_buy_model.joblib"


def build_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_COLUMNS),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_COLUMNS),
        ]
    )

    model = LogisticRegression(max_iter=1000, random_state=42)

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    return pipeline


def train_and_save_model(
    csv_path: Path = DEFAULT_CSV_PATH,
    model_path: Path = DEFAULT_MODEL_PATH,
) -> dict[str, float | int | str]:
    df = load_csv(csv_path)
    cleaned_df = clean_data(df)

    x = cleaned_df[FEATURE_COLUMNS]
    y = cleaned_df[TARGET_COLUMN]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    pipeline = build_pipeline()
    pipeline.fit(x_train, y_train)

    predictions = pipeline.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    model_path.parent.mkdir(parents=True, exist_ok=True)

    artifact = {
        "model": pipeline,
        "feature_columns": FEATURE_COLUMNS,
        "target_column": TARGET_COLUMN,
    }

    joblib.dump(artifact, model_path)

    return {
        "rows_after_cleaning": int(len(cleaned_df)),
        "train_rows": int(len(x_train)),
        "test_rows": int(len(x_test)),
        "accuracy": float(accuracy),
        "model_path": str(model_path),
    }


def main() -> None:
    report = train_and_save_model()

    print("Entrenamiento completado")
    print(f"Filas después de limpieza: {report['rows_after_cleaning']}")
    print(f"Filas de entrenamiento: {report['train_rows']}")
    print(f"Filas de prueba: {report['test_rows']}")
    print(f"Accuracy: {report['accuracy']:.4f}")
    print(f"Modelo guardado en: {report['model_path']}")


if __name__ == "__main__":
    main()
