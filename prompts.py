from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from pydantic import BaseModel, Field
from typing import List

class CarDealEvaluation(BaseModel):
    verdict: str = Field(description="Fair Deal, Overpriced, or Good Deal")
    red_flags: List[str] = Field(description="Top 3 red flags about this listing")
    questions: List[str] = Field(description="5 questions to ask the seller")
    negotiation_advice: str = Field(description="Counter offer suggestion and reasoning")

def get_prompt_template():
    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert in the Pakistani used car market.

        Evaluate this listing:
        - Car: {make} {model} {year}
        - Mileage: {mileage} km
        - Asking Price: PKR {asking_price}
        - City: {city}
        - Description: {car_deal_description}

        Provide a thorough evaluation covering verdict, red flags,
        questions for the seller, and negotiation advice.
        """,
        
    )
    return prompt