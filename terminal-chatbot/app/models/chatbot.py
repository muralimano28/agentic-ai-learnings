from typing import Literal, List
from pydantic import BaseModel, Field

class Chat(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str


class ChatHistory(BaseModel):
    history: List[Chat]

class JsonResponse(BaseModel):
    user_name: str = Field(description="The full name of the user. It includes first name and last name separated by space.")
    topic: str = Field(description="The main topic of the conversation.")
    sentiment: Literal["positive", "neutral", "negative"] = Field(description="The overall sentiment of the conversation.")
    summary: str = Field(description="A brief summary of the conversation.")
    company_name: str = Field(description="The company name of the user.")
    domain: str = Field(description="The domain of the user.")
    years_of_experience: int = Field(description="The number of years of experience of the user.")
    action_items: List[str] = Field(description="A list of action items identified during the conversation.")
    actual_response: str = Field(description="The actual response from the assistant.")
