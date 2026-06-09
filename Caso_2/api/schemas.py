from pydantic import BaseModel, Field
from typing import Optional

class StudentInput(BaseModel):
    horas_de_estudio: float = Field(..., ge=0, le=24, description="Horas de estudio por semana (0-24)")
    resultados_anteriores: float = Field(..., ge=0, le=100, description="Puntaje en evaluaciones anteriores (0-100)")
    extracurricular: int = Field(..., ge=0, le=1, description="Asiste a actividades extracurriculares (0=No, 1=Sí)")
    horas_sueno: float = Field(..., ge=0, le=24, description="Horas de sueño por noche (0-24)")
    num_ejercicios_resueltos: float = Field(..., ge=0, description="Ejercicios prácticos resueltos")

    class Config:
        json_schema_extra = {
            "example": {
                "horas_de_estudio": 3,
                "resultados_anteriores": 55,
                "extracurricular": 0,
                "horas_sueno": 5,
                "num_ejercicios_resueltos": 1
            }
        }

class PredictionOutput(BaseModel):
    rendimiento_bajo: bool
    probabilidad: float
    mensaje: str

class StudentRecord(BaseModel):
    id: int
    datos: StudentInput
    prediccion: Optional[PredictionOutput] = None
