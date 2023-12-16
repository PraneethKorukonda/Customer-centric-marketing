import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def preprocess_data(ARIMA_df):
    ARIMA_df['InvoiceDate'] = pd.to_datetime(ARIMA_df['InvoiceDate'])
    ARIMA_df.set_index('InvoiceDate', inplace=True)
    return ARIMA_df

def perform_curve_fitting(ARIMA_df):
    model = ARIMA(ARIMA_df['Daily Sales'], order=(7, 1, 7))
    results = model.fit()

    plt.figure(figsize=(15, 8))
    plt.plot(ARIMA_df.index, ARIMA_df['Daily Sales'], label='Original Data')
    plt.plot(ARIMA_df.index, results.fittedvalues, color='red', label='ARIMA Fitted Values')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()

    return plt, results

def perform_forecasting(ARIMA_df, forecast_steps):
    model = ARIMA(ARIMA_df['Daily Sales'], order=(7, 1, 7))
    results = model.fit()

    forecast = results.forecast(steps=forecast_steps)

    future_dates = pd.date_range(start=ARIMA_df.index[-1] + pd.Timedelta(days=1), periods=forecast_steps, freq='D')

    plt.figure(figsize=(15, 8))
    plt.plot(ARIMA_df.index, ARIMA_df['Daily Sales'], label='Original Data')
    plt.plot(future_dates, forecast, color='red', label='Forecast')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()

    return plt

def main():
    st.title('Sales Forecasting App')

    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        data = preprocess_data(data)
        st.write(data.head())

        st.subheader('ARIMA Curve Fitting')
        curve_fitting_plot, _ = perform_curve_fitting(data)
        st.pyplot(curve_fitting_plot)

        forecast_days = st.selectbox("Select forecast horizon (days)", [30, 45, 60, 90])

        st.subheader(f'Forecasting Results for {forecast_days} days')
        forecast_plot = perform_forecasting(data, forecast_days)
        st.pyplot(forecast_plot)

if __name__ == '__main__':
    main()
