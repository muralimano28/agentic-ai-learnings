from app import DocumentService, RetrievalService, EmbeddingService, StorageService
import numpy as np

class SearchApp:
    def __init__(self):
        # Initialize services inside the constructor to avoid side effects on module import
        self.document_service = DocumentService()
        self.embedding_service = EmbeddingService()
        self.storage_service = StorageService()
        
        # Dependency Injection: share same instances of embedding/storage services
        self.retrieval_service = RetrievalService(
            embedding_service=self.embedding_service,
            storage_service=self.storage_service
        )

    def run(self):
        print("Welcome to semantic search engine")
        
        # Create new embeddings and store them in the vector store
        chunks: list[str] = self.document_service.load_document_in_chunks()
        embeddings: np.ndarray = self.embedding_service.get_embeddings(chunks)
        
        self.storage_service.save_to_vector_store(embeddings, chunks)
        print("Embeddings stored in vector store")

        while True:
            query: str = input("Enter your query: ")
            if query.strip().lower() == "exit":
                break

            retrieved_documents = self.retrieval_service.search(query)
            print("Retrieved documents:", retrieved_documents)


def main():
    app = SearchApp()
    app.run()


if __name__ == "__main__":
    main()
