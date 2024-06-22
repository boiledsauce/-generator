from src.models.cover_letter_model import CoverLetterModel
from typing import List

def generate_cover_letter(job_description: str, cover_letters: List[str], api_key: str, cv: str) -> str:
    model = CoverLetterModel(api_key)
    return model.generate(job_description, cover_letters, cv)