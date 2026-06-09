from app.models.chatbot import JsonResponse
import os
from app.models.chatbot import Chat, ChatHistory
from google import genai
from google.genai import Client, types


gemini_api_key = os.environ.get("GEMINI_API_KEY")


class ChatbotService():
    def __init__(self) -> None:
        self.history: ChatHistory = []
        self.client: Client = genai.Client(api_key=gemini_api_key)
       
       
       # self.contentConfig = types.GenerateContentConfig(
            # response_mime_type="application/json", # This is for getting structured outputs
            # response_schema=Chat, # Structured outputs will follow this schema
            # system_instruction=(
            #     "You are a helpful terminal assistant.",
            #     "Keep your answers brief, informative and slightly witty."
            # ),
            # temperature=0.7  # If we are calling tools, then we need to set this as 0.0
        # )


        # client.chats.create is a stateful, multi-turn which manages automatic history.
        # this is best used for interactive applications where it preserves context.
        # self.chatbot = self.client.chats.create(  # Stateful / Multi-Turn
        #     model='gemini-3.1-flash-lite',
        #     config=self.contentConfig
        # )

        self.chatbot = None

    def get_content_config(
        self, 
        response_mime_type: str = None,
        response_schema: types.GenerateContentConfig.response_schema = None,
        system_instruction: str | tuple = (
            "You are a helpful terminal assistant.",
            "Keep your answers brief, informative and slightly witty."
        ),
        temperature: float = 0.7
    ) -> types.GenerateContentConfig:
        return types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=temperature,
            response_mime_type=response_mime_type,
            response_schema=response_schema
        )

    def get_response(
        self, 
        user_message: str,
        stateful: bool, 
        config: types.GenerateContentConfig = None, 
        model: str = 'gemini-3.1-flash-lite'
    ) -> types.GenerateContentResponse:
        if config is None:
            config = self.get_content_config()

        if stateful:
            if not self.chatbot:
                self.chatbot = self.client.chats.create(
                    model=model,
                    config=config
                )

            return self.chatbot.send_message(user_message)
        else:
            return self.client.models.generate_content(
                model=model,
                config=config,
                contents=user_message
            )

    def send_message(self, user_message: str, stateful: bool = False, structured_output: bool = False) -> Chat:
        user_chat = Chat(role="user", content=user_message)

        self.history.append(user_chat)

        config = None
        if structured_output:
            config = self.get_content_config(
                response_mime_type="application/json", 
                response_schema=JsonResponse
            )

        '''
            generate_content is a single, stateless request
            this is best used for single-turn tasks like summarization, extraction or translating a single sentence.
        '''
        # response = self.client.models.generate_content(  # stateless / One-Off
        #     model='gemini-3.1-flash-lite',
        #     contents=user_message,
        #     config=self.contentConfig
        # )

        '''
            client.chats.create is a stateful, multi-turn which manages automatic history.
            this is best used for interactive applications where it preserves context.
        '''
        # response = self.chatbot.send_message(user_message)


        response = self.get_response(user_message, stateful, config)

        bot_response: Chat = Chat(
            role="assistant", content=response.text)

        self.history.append(bot_response)

        return bot_response

    def close_client(self) -> None:
        self.client.close()
