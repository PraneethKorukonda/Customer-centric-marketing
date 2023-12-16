import pandas as pd
ARIMA_df = pd.read_csv('/Users/praneethkorukonda/Documents/ADM/Sales_Forecasting/ARIMA_df_1.csv')




import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Assuming 'ARIMA_df' is your DataFrame with 'Daily Sales' as the column name and 'Date' as a column

# Set 'Date' column as the DataFrame index
ARIMA_df['InvoiceDate'] = pd.to_datetime(ARIMA_df['InvoiceDate'])
ARIMA_df.set_index('InvoiceDate', inplace=True)

# Perform seasonal decomposition on the 'Daily Sales' column
decomposition = seasonal_decompose(ARIMA_df['Daily Sales'])

# Fit ARIMA model on the 'Daily Sales' column
model = ARIMA(ARIMA_df['Daily Sales'], order=(7, 1, 7))  # Example using p=7, d=1, q=7 (as observed)
results = model.fit()

# Plot the original 'Daily Sales' column and fitted values from ARIMA
plt.figure(figsize=(10, 6))
plt.plot(ARIMA_df.index, ARIMA_df['Daily Sales'], label='Original Data')
plt.plot(ARIMA_df.index, results.fittedvalues, color='red', label='ARIMA Fitted Values')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()



# Assuming 'ARIMA_df' is your time series data with missing values and the ARIMA model is already fitted

# Forecast sales for the next 36 months (adjust steps as needed)
forecast_steps = 45
forecast = results.forecast(steps=forecast_steps)

# Create a range of future dates for the forecast (assuming 'ARIMA_df' is monthly data)
future_dates = pd.date_range(start=ARIMA_df.index[-1], periods=forecast_steps, freq='D')

# Set a larger plot size
plt.figure(figsize=(15, 8))

# Plot the original data and the forecasted values
plt.plot(ARIMA_df.index, ARIMA_df, label='Original Data')  # Replace 'Sales' with your column name
plt.plot(future_dates, forecast, color='red', label='Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()


