import streamlit as st
from prompts import get_prompt_template, CarDealEvaluation
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

def evaluate_car(make, model, year, mileage, asking_price, city, car_deal_description):
    prompt = get_prompt_template()
    
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.3, groq_api_key=groq_api_key)
    structured_llm = llm.with_structured_output(CarDealEvaluation)

    chain = prompt | structured_llm
    
    result = chain.invoke({
        "make": make,
        "model": model,
        "year": year,
        "mileage": mileage,
        "asking_price": asking_price,
        "city": city,
        "car_deal_description": car_deal_description
    })
    
    return result

