"""
CRUD simulado con diccionario en memoria.
Principio SOLID: Single Responsibility — este módulo solo maneja
el almacenamiento de registros de estudiantes.
"""
from typing import Optional
from schemas import StudentInput, PredictionOutput, StudentRecord

# "Base de datos" en memoria
_db: dict[int, dict] = {}
_counter: int = 0


def create(data: StudentInput, prediccion: Optional[PredictionOutput] = None) -> StudentRecord:
    global _counter
    _counter += 1
    record = StudentRecord(id=_counter, datos=data, prediccion=prediccion)
    _db[_counter] = record.dict()
    return record


def read_one(student_id: int) -> Optional[StudentRecord]:
    entry = _db.get(student_id)
    return StudentRecord(**entry) if entry else None


def read_all() -> list[StudentRecord]:
    return [StudentRecord(**v) for v in _db.values()]


def update(student_id: int, data: StudentInput, prediccion: Optional[PredictionOutput] = None) -> Optional[StudentRecord]:
    if student_id not in _db:
        return None
    record = StudentRecord(id=student_id, datos=data, prediccion=prediccion)
    _db[student_id] = record.dict()
    return record


def delete(student_id: int) -> bool:
    return _db.pop(student_id, None) is not None


def count() -> int:
    return len(_db)
