import chromadb
from typing import List, Dict, Any

class DatabaseService:
    def __init__(self, path: str = "./knowledge_base", collection_name: str = "knowledge_base_search"):
        self.db_client = chromadb.PersistentClient(path=path)
        self.collection_name = collection_name
        self.collection = self.db_client.get_or_create_collection(name=self.collection_name)

    def ingest_chunks(self, chunks: List[Dict[str, Any]]):
        if not chunks:
            return
        
        ids = []
        documents = []
        metadatas = []
        
        for chunk in chunks:
            ids.append(chunk["id"])
            documents.append(chunk["content"])
            
            # Ensure metadata values are simple types (str, int, float, bool) for Chroma compatibility
            meta = chunk.get("meta", {})
            flat_meta = {}
            for k, v in meta.items():
                if isinstance(v, (str, int, float, bool)):
                    flat_meta[k] = v
                else:
                    flat_meta[k] = str(v)
            metadatas.append(flat_meta)

        self.collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

    def search_query(self, query: str, n_results: int = 3) -> Dict[str, Any]:
        return self.collection.query(
            query_texts=[query],
            n_results=n_results,
        )
