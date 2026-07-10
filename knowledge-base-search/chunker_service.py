import hashlib

class Chunker():
    def __init__(self):
        pass

    def split_content(self, content):
        pass

    '''
    Returns
    [{
        "id": "some-random-id",

        "content": "...",

        "metadata": {
            "title": "section-title-or-sub-section-title",
        }
    }]
    '''
    def create_chunks(self, doc: dict) -> list[dict]:
        type = doc["type"]
        content = doc["content"]
        title = doc["title"]

        child_chunks = []

        # traverse children
        for child in doc["children"]:
            child_chunks.extend(self.create_chunks(child))

        # process node
        if content:
            id = hashlib.md5(content.encode('utf-8')).hexdigest()
            if len(content) < 1200:
                return [{
                    "id": id,
                    "content": content,
                    "meta": {
                        "type": type,
                        "title": title,
                    }
                }, *child_chunks]
            else:
                #TODO: split by sentences and create multiple chunks
                id = hashlib.md5(content.encode('utf-8')).hexdigest()                
                return [
                    {
                        "id": id,
                        "content": content,
                        "meta": {
                            "type": type,
                            "title": title,
                        }
                    }, *child_chunks
                ]
        else:
            return child_chunks

        
        