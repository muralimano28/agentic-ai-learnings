from parser_service import Parser
from chunker_service import Chunker
from db_service import DatabaseService
from llm_service import LLMService
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

class KnowledgeBaseSearch():
    def __init__(self):
        self.file_path = "assets/acme_corp_policies_rag_test.pdf"
        self.parser = Parser()
        self.chunker = Chunker()
        self.db_service = DatabaseService()
        self.llm_service = LLMService()
    
    def extract_text(self):
        reader = PdfReader(self.file_path)
        pages = reader.pages
        text = ""

        for each_page in pages:
            text += "\n"
            text += each_page.extract_text()

        return text


    def get_query_from_user(self):
        query = input("Enter your query: ")
        return query.strip()

    def get_relevant_context(self, query: str):
        return self.db_service.search_query(query)

    def send_query_with_context_to_llm(self, query, context):
        documents = context["documents"][0]
        metadatas = context["metadatas"][0]

        llm_contents = []

        if documents and len(documents):
            llm_contents.append('context:')

            for idx, each_document in enumerate(documents):
                llm_contents.append(f"{each_document} source: {metadatas[idx]["title"]}")
            
        llm_contents.append('----')
        llm_contents.append('query:')
        llm_contents.append(query)

        contents = "\n".join(llm_contents)

        return self.llm_service.get_response(contents)

    def start_pipeline(self):
        extracted_text = self.extract_text()
        doc = self.parser.parse_text_to_dict(extracted_text)
        chunks = self.chunker.create_chunks(doc)

        self.db_service.ingest_chunks(chunks)

        while True:
            query = self.get_query_from_user()
            
            if (query is None or len(query) == 0):
                continue

            if (query == 'exit'):
                break

            context = self.get_relevant_context(query)
            response = self.send_query_with_context_to_llm(query, context)

            print(response)
        

def main():
    kbs = KnowledgeBaseSearch()
    kbs.start_pipeline()

if __name__ == "__main__":
    main()
