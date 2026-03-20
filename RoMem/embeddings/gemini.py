from configs.embeddings.base import BaseEmbeddingConfig
from typing import Literal
from base import BaseEmbedding

from google import genai
from google.genai import types

import os

class GeminiEmbedding(BaseEmbedding):
    
    def __init__(self, config: BaseEmbeddingConfig | None = None):
        super().__init__(config)

        if not self.config.model:
            self.config.model = "gemini-embedding-001"
        if not self.config.embed_dim:
            self.config.embed_dim = 768
        
        api_key = self.config.api_key or os.getenv("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def embed(self, text: list[str], memory_action: Literal["search", "update", "add"] | None = None):

        config = types.EmbedContentConfig(
            output_dimensionality = self.config.embed_dim
        )
        response = self.client.models.embed_content(
            model=self.config.model,
            contents=text,
            config=config
        )
        return response.embeddings
        

