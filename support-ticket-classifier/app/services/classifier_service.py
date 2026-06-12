from google import genai
import os
from app.models.classifier import OutputData
from google.genai import Client, types
from app.utils.helpers import get_system_instruction, get_examples

gemini_api_key = os.environ.get("GEMINI_API_KEY")

class ClassifierService():
    def __init__(self):
        self.client: Client = genai.Client(api_key=gemini_api_key)

    def get_content_config(self, use_json_output:bool = False) -> types.GenerateContentConfig:
        return types.GenerateContentConfig(
            response_mime_type="application/json" if use_json_output else "text/plain",
            response_schema=OutputData if use_json_output else None, # use response_schema for pydantic way and response_json_schema for RAW JSON.
            max_output_tokens=512 if use_json_output else 10, # Since we are generating the output in JSON format, we need more tokens
            temperature=0.0, # For deterministic outputs, keep it low
            system_instruction=get_system_instruction(use_json_output)
        )

    def get_prompt_with_examples(self, input_text:str, use_json_output:bool) -> str:
            # {get_examples(use_json_output)}
        
        return f"""
            Input: {input_text}
            Output: 
        """

    def classify(self, text:str, use_json_output:bool) -> str:
        message_content = self.get_prompt_with_examples(text, use_json_output)
       
        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            config=self.get_content_config(use_json_output),
            contents=message_content
        )


        if use_json_output:
            return OutputData.model_validate_json(response.text), response.usage_metadata

        return response.text, response.usage_metadata