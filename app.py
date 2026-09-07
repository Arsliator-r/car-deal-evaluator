import streamlit as st
from chain import evaluate_car

st.set_page_config(page_title="Car Deal Evaluator PK", 
                   page_icon="🚗")

st.title("🚗 Pakistani Car Deal Evaluator")
st.markdown("Paste your listing details and get an instant AI evaluation.")

col1, col2 = st.columns(2)

with col1:
    make = st.text_input("Make", placeholder="Toyota")
    model = st.text_input("Model", placeholder="Corolla")
    year = st.number_input("Year", min_value=1990, 
                            max_value=2025, value=2019)
    city = st.text_input("City", placeholder="Lahore")

with col2:
    mileage = st.number_input("Mileage (km)", min_value=0, 
                               value=80000)
    price = st.number_input("Asking Price (PKR)", 
                             min_value=0, value=3500000)

car_deal_description = st.text_area("Car Deal Description",
                                    placeholder="Well-maintained, low mileage, great condition.")    

if st.button("Evaluate This Deal", type="primary"):
    with st.spinner("Analysing listing..."):
        result = evaluate_car(make, model, year,
                              mileage, car_deal_description,
                              price, city)
        st.markdown("---")
        
        # Verdict as colored badge
        color = "green" if "Good" in result.verdict else \
                "red" if "Overpriced" in result.verdict else "orange"
        st.markdown(f"### Verdict: :{color}[{result.verdict}]")
        
        # Red flags as list
        st.markdown("### 🚩 Red Flags")
        for flag in result.red_flags:
            st.warning(flag)
        
        # Questions as numbered list
        st.markdown("### ❓ Questions to Ask Seller")
        for i, q in enumerate(result.questions, 1):
            st.markdown(f"{i}. {q}")
        
        # Negotiation advice
        st.markdown("### 💰 Negotiation Advice")
        st.info(result.negotiation_advice)