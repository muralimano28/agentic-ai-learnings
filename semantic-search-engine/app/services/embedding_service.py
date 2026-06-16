from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService():
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def get_embeddings(self, chunks: list[str]) -> np.ndarray:
        embeddings = self.model.encode(chunks, convert_to_numpy=True)

        return embeddings