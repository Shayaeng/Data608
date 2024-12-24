from fredapi import Fred
import matplotlib.pyplot as plt
import pandas as pd
from bls_data import BlsData

# Get your API keys
fred_api_key = '9399606b2ceeaa0a58491d4e6b122b15'
bls_api_key = '66993dba6faf49dfa7ae3cc335de3f9c'

# Set your FRED API key
fred = Fred(api_key=fred_api_key)

# Set your BLS API key
bls = BlsData(api_key=bls_api_key)

# Fetch data for the last 25 years
start_date = '1999-01-01'
end_date = '2024-01-01'

# Consumer Price Index (CPI) from FRED
cpi_fred = fred.get_series('CPIAUCSL', observation_start=start_date, observation_end=end_date)

# Unemployment Rate from FRED
unemployment_rate_fred = fred.get_series('UNRATE', observation_start=start_date, observation_end=end_date)

# Consumer Price Index (CPI) from BLS
cpi_bls = bls.get_series('CUUR0000SA0', start_year=1999, end_year=2024)

# Unemployment Rate from BLS
unemployment_rate_bls = bls.get_series('LNS14000000', start_year=1999, end_year=2024)

# Create a DataFrame
data = pd.DataFrame({
    'CPI_FRED': cpi_fred,
    'Unemployment Rate_FRED': unemployment_rate_fred,
    'CPI_BLS': cpi_bls,
    'Unemployment Rate_BLS': unemployment_rate_bls
})

# Plot the data
plt.figure(figsize=(14, 8))

# CPI Comparison
plt.subplot(2, 1, 1)
plt.plot(data.index, data['CPI_FRED'], label='CPI (FRED)', color='blue')
plt.plot(data.index, data['CPI_BLS'], label='CPI (BLS)', color='orange')
plt.title('Consumer Price Index (CPI) Comparison')
plt.ylabel('CPI')
plt.legend()

# Unemployment Rate Comparison
plt.subplot(2, 1, 2)
plt.plot(data.index, data['Unemployment Rate_FRED'], label='Unemployment Rate (FRED)', color='red')
plt.plot(data.index, data['Unemployment Rate_BLS'], label='Unemployment Rate (BLS)', color='purple')
plt.title('Unemployment Rate Comparison')
plt.ylabel('Rate (%)')
plt.legend()

plt.tight_layout()
plt.show()