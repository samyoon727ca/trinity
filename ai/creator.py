# creator.py
from langchain_community.llms import Ollama

class CreatorAI:
    def __init__(self):
        self.model = Ollama(model="llama3")

    def generate_idea(self, prompt):
        generated_text = self.model.invoke([prompt])
        return generated_text