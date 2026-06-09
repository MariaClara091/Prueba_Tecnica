import joblib
import numpy as np
from pathlib import Path
from schemas import StudentInput, PredictionOutput

# Rutas a los modelos
BASE_DIR    = Path(__file__).parent.parent
MODEL_PATH  = BASE_DIR / "models" / "best_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

# Cargar modelos al iniciar
try:
    model  = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print(f"[OK] Modelo cargado: {type(model).__name__}")
except Exception as e:
    raise RuntimeError(f"Error al cargar modelos: {e}")

# Orden de features igual al entrenamiento
FEATURES_ORDER = [
    "horas_de_estudio",
    "resultados_anteriores",
    "extracurricular",
    "horas_sueno",
    "num_ejercicios_resueltos"
]

def predict(data: StudentInput) -> PredictionOutput:
    """Aplica el modelo de Gradient Boosting y retorna la predicción."""
    X = np.array([[
        data.horas_de_estudio,
        data.resultados_anteriores,
        data.extracurricular,
        data.horas_sueno,
        data.num_ejercicios_resueltos
    ]])
    X_sc = scaler.transform(X)
    prob = float(model.predict_proba(X_sc)[0][1])
    bajo = prob >= 0.5

    if prob >= 0.75:
        mensaje = "🚨 Alto riesgo de bajo rendimiento — se recomienda intervención inmediata."
    elif prob >= 0.5:
        mensaje = "⚠️  Riesgo moderado de bajo rendimiento — monitoreo recomendado."
    else:
        mensaje = "✅ Sin riesgo de bajo rendimiento."

    return PredictionOutput(
        rendimiento_bajo=bajo,
        probabilidad=round(prob, 4),
        mensaje=mensaje
    )
