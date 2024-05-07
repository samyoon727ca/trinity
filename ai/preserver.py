# preserver.py
from langchain_community.llms import Ollama

class PreserverAI:
    def __init__(self):
        self.model = Ollama(model="llama3")

    def generate_preservation(self, input_text):
        prompt = f"{input_text}"
        generated_text = self.model.invoke([prompt])
        return generated_text