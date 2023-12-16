import streamlit as st
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

def train_xgboost_model(data):
    X = data.drop('NextPurchaseDayRange', axis=1)
    y = data['NextPurchaseDayRange']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=22)
    
    # Train the XGBoost model using X_train and y_train
    model = xgb.XGBClassifier()  # Replace with actual model initialization method
    model.fit(X_train, y_train)
    
    return model, X_test

def get_features_for_customer(customer_id, test_data):
    customer_features = test_data[test_data['CustomerID'] == customer_id].copy()  # Make a copy of the subset
    return customer_features

def classify_customer_segment(customer_features):
    # Check 'Segment' columns and classify the customer based on the values
    if customer_features['Segment_High-Value'].values[0] == 1:
        return "He comes under the category Infrequent Shopper"
    elif customer_features['Segment_Mid-Value'].values[0] == 1:
        return "He comes under the category Value-Conscious Shopper"
    elif customer_features['Segment_Low-Value'].values[0] == 1:
        return "He comes under the category Devoted Customer"
    else:
        return "Category not found"

st.title("Next Purchase Date")
st.sidebar.header("Next Purchase Date")
st.write("""Next Purchase Date!""")

# Load invoice_class.csv
invoice_class = pd.read_csv('invoice_class.csv')
# Replace with your file path

# Train XGBoost model and get X_test
trained_model, X_test = train_xgboost_model(invoice_class)

# Dropdown input for CustomerID
customer_ids = X_test['CustomerID'].unique().tolist()
selected_customer_id = st.selectbox('Select CustomerID:', customer_ids)

if st.button('Predict'):
    customer_id = int(selected_customer_id)
    customer_features = get_features_for_customer(customer_id, X_test)
    if len(customer_features) == 0:
        st.write("CustomerID not found in test data")
    else:
        prediction_result = trained_model.predict(customer_features)
        segment_classification = classify_customer_segment(customer_features)

        # Displaying both predictions
        if prediction_result == 0:
            st.write("NextPurchaseDay > 50")
        elif prediction_result == 1:
            st.write("NextPurchaseDay > 20")
        elif prediction_result == 2:
            st.write("NextPurchaseDay within 20 days")
        else:
            st.write("Unknown prediction result")

        # Displaying customer segment classification
        st.write("Customer Segment: ", segment_classification)

        # Display images based on segmentation class
        if segment_classification == "He comes under the category Infrequent Shopper":
            st.image("Infrequent_shoppers.png", caption='Infrequent Shoppers', use_column_width=True)
        elif segment_classification == "He comes under the category Value-Conscious Shopper":
            st.image("Value_conscious_Shoppers.png", caption='Value-Conscious Shopper', use_column_width=True)
        elif segment_classification == "He comes under the category Devoted Customer":
            st.image("Devoted_Shoppers.png", caption='Devoted Customer', use_column_width=True)
