"""
API FastAPI — Student Performance Predictor
Predice el riesgo de bajo rendimiento académico usando Gradient Boosting.

Principios SOLID aplicados:
- S: cada módulo tiene una sola responsabilidad (schemas, service, crud, main)
- O: nuevos modelos se agregan sin modificar service.py
- L: los schemas de entrada/salida son sustituibles
- I: endpoints pequeños y específicos
- D: main depende de abstracciones (service, crud), no de implementaciones directas
"""
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from schemas import StudentInput, PredictionOutput, StudentRecord
import service
import crud

app = FastAPI(
    title="Student Performance API",
    description=(
        "API para predecir el riesgo de bajo rendimiento académico "
        "usando un modelo de Gradient Boosting entrenado sobre el dataset "
        "Student Performance (Universidad Simón Bolívar)."
    ),
    version="1.0.0",
    contact={"name": "Caso Técnico — Ciencia de Datos"}
)


# ──────────────────────────────────────────
# PREDICCIÓN
# ──────────────────────────────────────────

@app.post(
    "/predict",
    response_model=PredictionOutput,
    summary="Predecir riesgo de bajo rendimiento",
    tags=["Predicción"]
)
def predict(student: StudentInput):
    """
    Recibe las características de un estudiante y retorna:
    - **rendimiento_bajo**: True si hay riesgo de bajo rendimiento
    - **probabilidad**: probabilidad estimada (0.0 - 1.0)
    - **mensaje**: interpretación del resultado
    """
    try:
        return service.predict(student)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en predicción: {str(e)}")


# ──────────────────────────────────────────
# CRUD DE ESTUDIANTES
# ──────────────────────────────────────────

@app.post(
    "/students",
    response_model=StudentRecord,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar estudiante y predecir",
    tags=["Estudiantes"]
)
def create_student(student: StudentInput):
    """Registra un estudiante, ejecuta la predicción y almacena el resultado."""
    prediccion = service.predict(student)
    return crud.create(student, prediccion)


@app.get(
    "/students",
    response_model=list[StudentRecord],
    summary="Listar todos los estudiantes registrados",
    tags=["Estudiantes"]
)
def get_all_students():
    """Retorna todos los registros almacenados en memoria."""
    return crud.read_all()


@app.get(
    "/students/{student_id}",
    response_model=StudentRecord,
    summary="Obtener un estudiante por ID",
    tags=["Estudiantes"]
)
def get_student(student_id: int):
    """Retorna el registro de un estudiante específico."""
    record = crud.read_one(student_id)
    if not record:
        raise HTTPException(status_code=404, detail=f"Estudiante con ID {student_id} no encontrado.")
    return record


@app.put(
    "/students/{student_id}",
    response_model=StudentRecord,
    summary="Actualizar datos de un estudiante",
    tags=["Estudiantes"]
)
def update_student(student_id: int, student: StudentInput):
    """Actualiza los datos de un estudiante y recalcula la predicción."""
    prediccion = service.predict(student)
    record = crud.update(student_id, student, prediccion)
    if not record:
        raise HTTPException(status_code=404, detail=f"Estudiante con ID {student_id} no encontrado.")
    return record


@app.delete(
    "/students/{student_id}",
    summary="Eliminar un estudiante",
    tags=["Estudiantes"]
)
def delete_student(student_id: int):
    """Elimina el registro de un estudiante."""
    if not crud.delete(student_id):
        raise HTTPException(status_code=404, detail=f"Estudiante con ID {student_id} no encontrado.")
    return {"message": f"Estudiante {student_id} eliminado correctamente."}


# ──────────────────────────────────────────
# HEALTH CHECK
# ──────────────────────────────────────────

@app.get("/", tags=["Health"])
def root():
    return {
        "status": "ok",
        "modelo": type(service.model).__name__,
        "estudiantes_registrados": crud.count(),
        "docs": "/docs"
    }
