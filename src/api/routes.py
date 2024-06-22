import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.generator import generate_cover_letter
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter()

COVER_LETTERS_DIR = os.getenv('COVER_LETTERS_DIR', '/app/cover_letters')

def read_cover_letters():
    cover_letters = []
    try:
        for filename in os.listdir(COVER_LETTERS_DIR):
            if filename.endswith(".txt"):
                with open(os.path.join(COVER_LETTERS_DIR, filename), 'r') as file:
                    cover_letters.append(file.read())
    except Exception as e:
        logger.error(f"Error reading cover letter files: {e}")
        raise
    return cover_letters

# Load cover letters when the app starts
COVER_LETTERS = read_cover_letters()

class JobApplication(BaseModel):
    job_description: str
    cv: str

@router.post("/generate")
async def generate_cover_letter_route(application: JobApplication):
    try:
        logger.debug("Received job description: %s", application.job_description)
        logger.debug("Received CV: %s", application.cv)
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found")
        
        logger.debug("API key found")

        # Generate cover letter content using job description and CV
        cover_letter = generate_cover_letter(application.job_description, COVER_LETTERS, api_key, application.cv)
        logger.debug(f"Generated cover letter: {cover_letter}")
        
        return {"cover_letter": cover_letter}
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
