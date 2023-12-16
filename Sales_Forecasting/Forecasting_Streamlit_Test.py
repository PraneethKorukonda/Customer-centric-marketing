import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def perform_forecasting(ARIMA_df, forecast_steps):
    # Assuming 'ARIMA_df' is your DataFrame with 'Date' and 'Daily Sales' columns
    ARIMA_df['InvoiceDate'] = pd.to_datetime(ARIMA_df['InvoiceDate'])
    ARIMA_df.set_index('InvoiceDate', inplace=True)

    # Assuming 'results' contains the fitted ARIMA model
    results = ARIMA(ARIMA_df['Daily Sales'], order=(7, 1, 7)).fit()

    # Forecast sales for the selected number of days
    forecast = results.forecast(steps=forecast_steps)

    # Create a range of future dates for the forecast
    future_dates = pd.date_range(start=ARIMA_df.index[-1], periods=forecast_steps, freq='D')

    # Plotting the forecast
    plt.figure(figsize=(15, 8))
    plt.plot(ARIMA_df.index, ARIMA_df['Daily Sales'], label='Original Data')
    plt.plot(future_dates, forecast, color='red', label='Forecast')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()

    return plt

def main():
    st.title('Sales Forecasting App')

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data.head())

        # Dropdown for selecting forecast horizon
        forecast_days = st.selectbox("Select forecast horizon (days)", [30, 45, 60, 90])

        # Perform forecasting on uploaded data for the selected horizon
        st.subheader(f'Forecasting Results for {forecast_days} days')
        forecast_plot = perform_forecasting(data, forecast_days)
        st.pyplot(forecast_plot)

if __name__ == '__main__':
    main()
