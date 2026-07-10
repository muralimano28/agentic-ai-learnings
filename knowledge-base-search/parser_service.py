import re

class Parser():
    def __init__(self):
        # Pre-compile the regular expressions once at the class/module level
        self.SECTION_REGEX = re.compile(r"^\d+\.\s")
        self.SUB_SECTION_REGEX = re.compile(r"^\d+\.\d+\s")
        self.FOOTER_REGEX = re.compile(r"Page\s\d+\sof\s\d+$")

    def pre_process(self, text):
        lines = text.split('\n')

        cleaned_lines = []
        footer_regex = r"Page\s\d+\sof\s\d+$"
        
        for line in lines:
            stripped_line = line.strip()
            is_footer = bool(self.FOOTER_REGEX.search(stripped_line))

            if stripped_line and not is_footer:
                cleaned_lines.append(stripped_line)
        
        return cleaned_lines

    def parse_text_to_dict(self, text: str) -> dict:
        lines = self.pre_process(text)

        if not lines:
            return {}

        # 1. Initialize the document node
        doc_title = lines[0]
        doc_node = {
            "type": "document",
            "id": "some-random-id",
            "title": doc_title,
            "content": [],
            "children": []
        }

        # The stack tracks the active path of nodes: [document_node, current_section_node, current_subsection_node]
        # We store references so we can modify them in-place.
        stack = [doc_node]

        for line in lines[1:]:
            # Check node boundaries
            is_section = bool(self.SECTION_REGEX.match(line))
            is_sub_section = bool(self.SUB_SECTION_REGEX.match(line))

            if is_section:
                # 2. Section node: pop stack until only the document node is left
                while len(stack) > 1:
                    stack.pop()
                
                new_section = {
                    "type": "section",
                    "id": "some-random-id",
                    "title": line,
                    "content": [],
                    "children": []
                }
                # Add as a child of the document
                stack[0]["children"].append(new_section)
                stack.append(new_section)

            elif is_sub_section:
                # 3. Sub-section node: pop stack until the current section is at the top
                # If we are deep in a sub-section, we pop back to the section level (length 2)
                while len(stack) > 2:
                    stack.pop()
                
                new_sub_section = {
                    "type": "sub_section",
                    "id": "some-random-id",
                    "title": line,
                    "content": [],
                    "children": []
                }
                
                # If a sub-section appears before any section is defined, attach it to the document
                parent = stack[-1]
                parent["children"].append(new_sub_section)
                stack.append(new_sub_section)

            else:
                # 4. Content line: append to the current active node at the top of the stack
                stack[-1]["content"].append(line)

        # 5. Post-process to join content lines into a single string (just like the original " ".join(rest))
        self.post_process(doc_node)
        
        return doc_node

    def post_process(self,node):
        node["content"] = " ".join(node["content"])
        
        for child in node["children"]:
            self.post_process(child)
