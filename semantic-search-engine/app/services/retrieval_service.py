from app.services.embedding_service import EmbeddingService
from app.services.storage_service import StorageService
from sentence_transformers import util

class RetrievalService():
    def __init__(self, embedding_service: EmbeddingService, storage_service: StorageService):
        self.embedding_service = embedding_service
        self.storage_service = storage_service

    def search(self, query: str):
        if len(query.strip()) == 0:
            return []

        query_embedding = self.embedding_service.get_embeddings([query])
        documents, embeddings = self.storage_service.load_from_vector_store()

        if len(documents) == 0 or embeddings.size == 0:
            return []
        
        # Compute cosine similarity between the query and all embeddings
        similarities = util.cos_sim(query_embedding, embeddings)[0]

        # Convert similarities tensor to numpy and pair with documents
        scores = similarities.cpu().numpy()
        results = []
        for doc, score in zip(documents, scores):
            results.append({
                "document": doc,
                "score": float(score)
            })
            
        # Sort results by similarity score in descending order
        results.sort(key=lambda x: x["score"], reverse=True)
        
        return results[:5]