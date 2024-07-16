# chat/services.py
from transformers import pipeline

class HuggingFaceService:
    def __init__(self, model_name):
        self.generator = pipeline('text-generation', model=model_name)

    def generate_response(self, prompt):
        return self.generator(prompt, max_length=100)[0]['generated_text']
