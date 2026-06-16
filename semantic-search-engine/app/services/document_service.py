class DocumentService():
    def __init__(self):
        pass

    def load_document_in_chunks(self) -> list[str]:
        return [
            "Traditional search engines rely heavily on keyword matching, which often fails to capture the underlying meaning.",
            "Semantic search solves keyword limitations by understanding the context and relationships between words.",
            "The sentence-transformers Python library allows developers to generate dense vector representations or embeddings.",
            "Embeddings map text into a continuous vector space where semantically similar texts are placed close together.",
            "Systems use metrics like Cosine Similarity to measure the distance between two semantic vectors.",
            "Applications of embeddings include semantic search, automated clustering, and paraphrase mining."
        ]
