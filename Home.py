import streamlit as st

st.set_page_config(
    page_title="Project Title",
    page_icon="👋",
)



st.title("Welcome to our App!")

st.write("""
    ### Introduction:
    This interactive platform provides insights and tools to analyze customer behavior, predict future purchases, forecast sales trends, and devise effective promotional strategies.
    
    ### Key Functionalities:
    - **RFM Analysis:**
        Analyze customer segments using Recency, Frequency, and Monetary Value metrics to understand their behavior.
    
    - **Next Purchase Date Prediction:**
        Predict when customers are likely to make their next purchase based on historical data.
                
        - **Promotional Strategies:**
        Discover effective promotional tactics and strategies based on Next Purchase Date adn Customer Segments.   
                    
    - **Sales Forecasting:**
        Predict future sales trends and patterns to optimize inventory and plan for future business strategies.
    
    ### Get Started:
    Dive into the functionalities using the navigation bar on the left or by clicking the buttons below.
    """)