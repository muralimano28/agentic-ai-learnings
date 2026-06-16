# import faiss
from app.services import embedding_service
import numpy as np
import json
import os

class StorageService():
    def __init__(self):
        self.storage_path = 'data/embeddings.json'
        
        """
        Always create a fresh storage when class is initialized.
        """
        if os.path.exists(self.storage_path):
            os.remove(self.storage_path)

    def save_to_vector_store(self, vectors: np.ndarray, documents: list[str]):
        """
        Store to a json file in the data folder
        """
        new_embeddings = []
        for vector, document in zip(vectors, documents):
            new_embeddings.append({
                "document": document,
                "vector": vector.tolist(),
            })

        embeddings = []
        if os.path.exists("data/embeddings.json"):
            with open("data/embeddings.json", "r") as f:
                embeddings = json.load(f)
        
        embeddings.extend(new_embeddings)

        with open("data/embeddings.json", "w") as f:
            json.dump(embeddings, f, indent=4)
    

    def load_from_vector_store(self) -> tuple[list[str], np.ndarray]:
        """
        Load from a json file in the data folder
        """
        embeddings = []
        if os.path.exists("data/embeddings.json"):
            with open("data/embeddings.json", "r") as f:
                embeddings = json.load(f)
        

        if not embeddings:
            return [], np.array([])
        
        """
        The saved embeddings are stored in JSON as text. 
        When json.load() reads them, Python represents these numbers as Python's standard 64-bit floating point numbers.
        However, the SentenceTransformer model expects float32 (single precision) vectors. 
        If we pass float64 vectors to the model, we'll get a runtime error.
        Therefore, we explicitly convert the vectors to float32 when creating the numpy array.
        """
        vectors = np.array([item["vector"] for item in embeddings], dtype=np.float32)
        documents = [item["document"] for item in embeddings]
        
        return documents, vectors

        

        
        