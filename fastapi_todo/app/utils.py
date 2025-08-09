# app/utils.py
from fastapi import HTTPException

def obtener_o_404(objeto, nombre="Recurso"):
    if objeto is None:
        raise HTTPException(status_code=404, detail=f"{nombre} no encontrado")
    return objeto
