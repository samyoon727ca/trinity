# destroyer.py
from langchain_community.llms import Ollama

class DestroyerAI:
    def __init__(self):
        self.model = Ollama(model="llama3")

    def generate_destruction(self, input_text):
        prompt = f"Destroyer: {input_text}"
        generated_text = self.model.invoke([prompt])
        return generated_text