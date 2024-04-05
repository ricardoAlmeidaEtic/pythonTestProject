import requests
import json 
from models import OllamaPrompt, OllamaResponse

class OllamaAPI:

    def __init__(self) -> None:
        self.base_url="http://ollama:11434"
        self.prompt_endpoint="api/generate"

    async def prompt(self, prompt: OllamaPrompt) ->OllamaResponse:
        assert prompt

        # Make the request to the Ollama API
        response: requests.Response = requests.get(
            url=f'{self.base_url}/{self.prompt_endpoint}',
            json=prompt.model_dump_json()
        )

        #response.raise_for_status()  # Raise an exception for HTTP errors
        
        return OllamaResponse(
            done = response.get("done").toString(),
            response = response.get("response").toString()
        )    
