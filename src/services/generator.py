from src.models.cover_letter_model import CoverLetterModel
from src.services.preprocessor import preprocess_text

def generate_cover_letter(job_description: str) -> str:
    preprocessed_job = preprocess_text(job_description)
    model = CoverLetterModel()
    return model.generate(preprocessed_job)