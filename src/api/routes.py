from fastapi import APIRouter, HTTPException
from src.services.generator import generate_cover_letter
from pydantic import BaseModel

router = APIRouter()

class JobDescription(BaseModel):
    description: str

@router.post("/generate")
async def generate_cover_letter_route(job: JobDescription):
    try:
        cover_letter = generate_cover_letter(job.description)
        return {"cover_letter": cover_letter}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))