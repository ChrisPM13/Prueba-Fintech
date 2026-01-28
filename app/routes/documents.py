from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
import os

from ..database import SessionLocal
from ..models import Document, Application
from ..services.ai_service import extract_info_from_text

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/applications/{application_id}/documents")
async def upload_document(
    application_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Validar tipo de archivo
    ALLOWED_TYPES = ["application/pdf", "image/jpeg", "image/png"]
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Tipo de archivo no permitido. Solo PDF o imagen (jpg/png)."
        )

    # Guardar archivo
    file_path = f"{UPLOAD_DIR}/{application_id}_{file.filename}"
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    # Obtener aplicación
    application = db.query(Application).filter(Application.id == application_id).first()

    # Extraer info usando el mock desde ai_service
    extracted = extract_info_from_text(application)

    # Guardar documento
    doc = Document(
        application_id=application_id,
        file_path=file_path,
        extracted_name=extracted["nombre"],
        extracted_address=extracted["direccion"],
        extracted_date=extracted["fecha"]
    )
    db.add(doc)
    db.commit()

    return {
        "message": "Documento guardado",
        "extracted": extracted
    }
