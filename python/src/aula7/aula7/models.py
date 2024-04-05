from typing import Literal
from pydantic import BaseModel

class OllamaPrompt(BaseModel):

    mode: Literal['gemma']
    prompt: str
    stream: bool = False