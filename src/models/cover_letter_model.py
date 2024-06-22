import openai
import random
from typing import List

class CoverLetterModel:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.system_prompt = """
        You are an AI assistant that generates personalized cover letters. 
        Your task is to create a cover letter that matches the style and tone of the provided examples, 
        while tailoring the content to the specific job description provided.
        """

    def prepare_examples(self, cover_letters: List[str], num_examples: int = 3) -> str:
        """Select a subset of cover letters to use as examples."""
        selected_letters = random.sample(cover_letters, min(num_examples, len(cover_letters)))
        return "\n\n--- Example Cover Letter ---\n\n".join(selected_letters)

    def generate(self, job_description: str, cover_letters: List[str], cv: str) -> str:
        examples = self.prepare_examples(cover_letters)
        
        prompt = f"""
        Here are examples of my previous cover letters:

        {examples}

        Now, please write a new cover letter for the following job description, maintaining my writing style:

        Job Description:
        {job_description}

        CV:
        {cv}

        The new cover letter should:
        1. Match the tone and style of the example letters
        2. Include an introduction that grabs attention
        3. Highlight relevant skills and experience from my CV, tailored to the job description
        4. Explain why I'm interested in this specific position and company
        5. End with a strong closing statement
        6. Be between 250-400 words

        Please ensure the letter sounds natural, personalized, and not generic. Use specific phrases or sentence structures from the example letters where appropriate.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  # This is GPT-4 Turbo
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response.choices[0].message['content'].strip()
