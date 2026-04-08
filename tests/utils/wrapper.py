import requests

class ModelClient:
    def __init__(self, model_name):
        self.base_url = "http://localhost:11434/"
        self.model_name = model_name

    def generate_answer(self, image_in_b64, question):
        response = requests.post(f"{self.base_url}/api/generate", json={
            "images":  [image_in_b64],
            "prompt": question,
            "model": self.model_name,
            "stream": False
        })   
        response = response.json()['response']
        
        return response