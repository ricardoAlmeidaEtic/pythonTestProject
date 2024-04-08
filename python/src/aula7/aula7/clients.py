import requests
import json
from models import OllamaPrompt, OllamaResponse

class OllamaAPI:

    def __init__(self) -> None:
        self.base_url="http://ollama:11434"
        self.prompt_endpoint="api/generate"

    async def prompt(self, prompt: OllamaPrompt):
        assert prompt

        # Make the request to the Ollama API
        response = requests.post(
            f'{self.base_url}/{self.prompt_endpoint}',
            json={
                'model': prompt.model,
                'prompt': prompt.prompt,
                'stream': prompt.stream
            }
        )

        try:
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json().get('response', None)
        except requests.exceptions.HTTPError as err:
            print("HTTP error:", err)
            print("Response content:", response.content)
            return "Error: Failed to get a valid response from the server."
        except json.decoder.JSONDecodeError as err:
            print("JSON decode error:", err)
            print("Response content:", response.content)
            return "Error: Failed to parse the response as JSON."
