from pydantic import BaseModel, Field

class GoogleSearchSnippet(BaseModel):
    title: str = Field(..., description="Title of the snippet.")
    metadescription: str = Field(..., description="Meta description of the snippet.")
    
