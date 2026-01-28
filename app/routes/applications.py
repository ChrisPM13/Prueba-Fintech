from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Application, Decision
from ..schemas import ApplicationCreate
from ..services.rule_engine import evaluate
import random

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/applications")
def create_application(data: ApplicationCreate, db: Session = Depends(get_db)):
    application = Application(**data.dict())
    db.add(application)
    db.commit()
    db.refresh(application)

    #  Aqui se obtiene el score
    score = random.randint(300, 900)
    application.credit_score = score

    # Se evaluan las reglas
    approved, decisions = evaluate(application, score)

    # Se guardan las decisiones
    explanation_parts = []

    for rule_name, result in decisions:
        decision = Decision(
            application_id=application.id,
            rule_name=rule_name,
            result=str(result),
            reason="Cumple" if result else "No cumple"
        )
        db.add(decision)

        explanation_parts.append(
            f"{rule_name}: {'cumple' if result else 'no cumple'}"
        )

    # Estado final
    application.status = "APPROVED" if approved else "REJECTED"
    
    # Explicacion 
    explanation = (
        f"La solicitud fue {'aprobada' if approved else 'rechazada'} porque: "
        + ", ".join(explanation_parts)
    )
    application.explanation = explanation
    db.commit()
    

    return {
        "application_id": application.id,
        "status": application.status,
        "credit_score": score,
        "explanation": explanation
    }


@router.get("/applications/{id}")
def get_application(id: int, db: Session = Depends(get_db)):
    application = db.query(Application).filter(Application.id == id).first()
    return application
