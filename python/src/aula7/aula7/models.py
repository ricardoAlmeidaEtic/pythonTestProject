from typing import Literal
from pydantic import BaseModel

class OllamaPrompt(BaseModel):

    mode: str = 'gemma:2b'
    prompt: str
    stream: bool = False

class OllamaResponse(BaseModel):

    done: str 
    response: str