import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:\\Stocks\\ZOMATO LTD\\ZOMATO.NS_5year_history.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
df.head(), df.info()


# Convert the Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Get summary statistics for the numerical columns in the dataset
summary_stats = df.describe()
print(summary_stats)

# Plotting the Close price over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], color='blue', label='Close Price')
plt.title('Stock Index - Close Price Trend Over the Last 5 Years')
plt.xlabel('Date')
plt.ylabel('Close Price (INR)')
plt.grid(True)
plt.legend()
plt.show()

# Calculate daily returns
df['Daily Return'] = df['Close'].pct_change()

# Calculate volatility (standard deviation of daily returns)
volatility = df['Daily Return'].std()

# Plotting the daily returns to visualize volatility
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Daily Return'], color='red', label='Daily Return')
plt.title('Stock Index - Daily Returns (Volatility) Over the Last 5 Years')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.grid(True)
plt.legend()
plt.show()

print('Volatility (Standard Deviation of Daily Returns):', volatility)


# Advanced Analysis
# Calculate the moving average (e.g., 50-day and 200-day moving averages)
df['50_MA'] = df['Close'].rolling(window=50).mean()
df['200_MA'] = df['Close'].rolling(window=200).mean()

# Plotting the Close price and moving averages
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
plt.plot(df['Date'], df['50_MA'], label='50-Day Moving Average', color='orange')
plt.plot(df['Date'], df['200_MA'], label='200-Day Moving Average', color='green')
plt.title('Stock Index - Moving Average Analysis')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.grid(True)
plt.legend()
plt.show()

# Extract the year from the Date column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Calculate yearly performance
yearly_performance = df.groupby('Year')['Close'].agg(['first', 'last'])
yearly_performance['Yearly Return (%)'] = ((yearly_performance['last'] - yearly_performance['first']) / yearly_performance['first']) * 100

print(yearly_performance)

# Calculate monthly returns
monthly_returns = df.pivot_table(index='Year', columns='Month', values='Daily Return', aggfunc=lambda x: ((x + 1).prod() - 1) * 100)

# Plotting the heatmap

plt.figure(figsize=(10, 6))
sns.heatmap(monthly_returns, annot=True, cmap='RdYlGn', fmt=".2f", linewidths=0.5)
plt.title('Monthly % Returns for Stock (Heat Map)')
plt.show()

# Group data by month to find seasonal patterns
df['Month'] = df['Date'].dt.month
monthly_avg = df.groupby('Month')['Close'].mean()

# Plotting the seasonal pattern
plt.figure(figsize=(10, 6))
monthly_avg.plot(kind='bar', color='purple')
plt.title('Stock Index - Seasonal Patterns in Monthly Average Close Prices')
plt.xlabel('Month')
plt.ylabel('Average Close Price (INR)')
plt.grid(True)
plt.show()