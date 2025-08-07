from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")  # Langchain will make use of the description
    facts: List[str] = Field(description="interesting facts about the person")

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Pydantic model to a dictionary."""
        return {"summary": self.summary, "facts": self.facts}


summary_parser = PydanticOutputParser(pydantic_object=Summary)

