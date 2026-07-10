import os
from google import genai

class LLMService:
    DEFAULT_SYSTEM_INSTRUCTION = f'''
        You are an expert assistant that answers questions accurately using ONLY the provided context.

        CRITICAL RULES FOR PERFORMANCE:
        1. STRICT ADHERENCE: Rely only on the clear facts directly mentioned in the context. Do not assume, extrapolate, or bring in outside knowledge.
        2. MISSING INFORMATION: If the context does not contain the answer, state exactly: "I cannot answer this based on the provided information." Do not attempt to guess or use general knowledge.
        3. CONTEXT OVERRIDE: If the context contradicts your pre-existing knowledge, prioritize the context completely.
        4. CITATION REQUIREMENT: Support every factual claim with a direct reference or bracketed index from the context source.
        5. BREVITY: Keep answers concise, factual, and directly relevant to the user query. Remove conversational filler.
    '''
    DEFAULT_TEMP = 0.0

    def __init__(self):
        gemini_api_key = os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=gemini_api_key)

    def get_response(self, contents, system_instruction = None, temp = None):
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents={
                'text': contents
            },
            config={
                'system_instruction': system_instruction or self.DEFAULT_SYSTEM_INSTRUCTION,
                'temperature': temp or self.DEFAULT_TEMP,
                # 'max_output_tokens': 1000
            }
        )

        return response.text




