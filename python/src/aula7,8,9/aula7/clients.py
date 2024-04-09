import requests
import json
from models import OllamaPrompt, OllamaResponse

class OllamaAPI:

    def __init__(self) -> None:
        self.base_url="http://ollama:11434"
        self.prompt_endpoint="api/generate"

    async def prompt(self, prompt: OllamaPrompt):
        assert prompt

        try:

            response: requests.Response = requests.post(
                url=f"{self.base_url}/{self.prompt_endpoint}",
                data=prompt.model_dump_json()
            )

            response.raise_for_status()

            return OllamaResponse(
                done=response.json().get('done', False),
                response=response.json().get('response', None)
            )
        
        except requests.exceptions.HTTPError as err:
            print("HTTP error:", err)
            print("Response content:", response.content)
            return "Error: Failed to get a valid response from the server."
        except json.decoder.JSONDecodeError as err:
            print("JSON decode error:", err)
            print("Response content:", response.content)
            return "Error: Failed to parse the response as JSON."
