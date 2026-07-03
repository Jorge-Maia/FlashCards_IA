import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

class GeradorIA:
    def __init__(self, modelo="gemini-2.5-flash"):
        self.client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        self.modelo = modelo

    def gerar_flashcards(self, tema, quantidade=5):
        prompt = f"""Gere exatamente {quantidade} flashcards de estudo sobre o tema "{tema}".
Responda APENAS com um JSON válido, sem nenhum texto antes ou depois, no formato:
[
  {{"pergunta": "...", "resposta": "..."}},
  ...
]"""
        resposta = self.client.models.generate_content(
            model=self.modelo,
            contents=prompt
        )

        texto = resposta.text.strip()
        texto = texto.removeprefix("```json").removesuffix("```").strip()

        return json.loads(texto)