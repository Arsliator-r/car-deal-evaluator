from prompts import get_prompt_template, CarDealEvaluation
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def evaluate_car(make, model, year, mileage, asking_price, city, car_deal_description):
    prompt = get_prompt_template()
    
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.3)
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

result = evaluate_car(
    make="Toyota",  
    model="Corolla",
    year=2020,
    mileage=50000,
    asking_price=2500000,
    city="Karachi",
    car_deal_description="Well-maintained, low mileage, great condition."
)

print("Verdict:", result.verdict)
print("Red Flags:", result.red_flags)
print("Questions for Seller:", result.questions)
print("Negotiation Advice:", result.negotiation_advice)
