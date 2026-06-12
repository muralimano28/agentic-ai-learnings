from typing import List
from pydantic import BaseModel, Field


class InputData(BaseModel):
    """
    Note: Ellipsis (...) in the Field means, it is a required field. When it is optional, we can send default=None
    """
    issue_description: str = Field(..., description="Description of the user's issue", min_length=1)

class OutputData(BaseModel):
    # Keep reasoning as the FIRST field so that the model thinks before deciding and don't skip this field.  
    # This is CoT - Chain-of-Thought technique
    reasoning: str = Field(..., description="Think step-by-step here. Analyze trap keywords versus the user's actual underlying intent.")
    
    given_issue_description: str = Field(..., description="Given input description of the user's issue", min_length=1)
    
    suggested_categories: List[str] = Field(..., description="List of suggested categories for the issue")