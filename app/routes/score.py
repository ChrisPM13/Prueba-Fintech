import random
from fastapi import APIRouter

router = APIRouter()


@router.get("/scorecredito")
def get_score():
    score = random.randint(300, 900)
    return {"score": score}
